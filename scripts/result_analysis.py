import matplotlib.pyplot as plt
import os
import csv

from agent_expt_suite.eval_utils.mbpp_plus import compare_dict_statuses, get_overall_status
from cognitive_base.utils import load_json

def calculate_accuracy(eval_results):
    """Calculate accuracy from evaluation results"""
    total = len(eval_results['eval'])
    correct = sum(1 for v in eval_results['eval'].values() 
                 if get_overall_status([v[0]['base_status'], v[0]['plus_status']]) == 'pass')
    return correct / total if total > 0 else 0

def load_experiment_results(model):
    """Load results for all methods for a given model"""
    results = {}
    
    # Zero shot (hardcoded results) from https://evalplus.github.io/leaderboard.html
    if model == '4_1106':
        # 277/378
        results['zero_shot'] = 0.733
    else:  # 4o_mini 273/378
        results['zero_shot'] = 0.722
        
    # ReAct
    react_folder = f'react_test_{model}'
    react_results = load_json(f'./final_results/{react_folder}/samples_eval_results.json')
    results['react'] = calculate_accuracy(react_results)
    
    # Voyager
    voyager_folder = f'voyager_proc_4_1106_test_{model}'
    voyager_results = load_json(f'./final_results/{voyager_folder}/samples_eval_results.json')
    results['voyager'] = calculate_accuracy(voyager_results)
    
    return results, react_results, voyager_results

def plot_accuracies():
    """Plot accuracy comparison for all methods and models"""
    models = ['4o_mini', '4_1106']
    methods = ['zero_shot', 'react', 'voyager']
    
    # Hardcoded counts for zero-shot
    zero_shot_counts = {
        '4_1106': (277, 378),  # (correct, total)
        '4o_mini': (273, 378)
    }
    
    # Collect all results
    all_results = {}
    eval_results = {}  # Store eval results for later comparison
    for model in models:
        all_results[model], react_results, voyager_results = load_experiment_results(model)
        eval_results[model] = {
            'react': react_results,
            'voyager': voyager_results
        }
    
    # Create plot
    plt.figure(figsize=(10, 6))
    bar_width = 0.2  # Slightly wider bars
    
    # Calculate positions for bars
    n_methods = len(methods)
    n_models = len(models)
    group_width = bar_width * n_methods
    group_positions = [i for i in range(n_models)]
    
    for i, method in enumerate(methods):
        accuracies = [all_results[model][method] * 100 for model in models]
        # Calculate bar positions relative to group center
        bar_positions = [x - group_width/2 + bar_width * (i + 0.5) for x in group_positions]
        
        bars = plt.bar(bar_positions, accuracies, bar_width, 
                      label=method.replace('_', ' ').title())
        
        # Add accuracy labels with counts on bars
        for j, (model, bar) in enumerate(zip(models, bars)):
            if method == 'zero_shot':
                correct, total = zero_shot_counts[model]
            else:
                results = eval_results[model][method]
                total = len(results['eval'])
                correct = sum(1 for v in results['eval'].values() 
                            if get_overall_status([v[0]['base_status'], v[0]['plus_status']]) == 'pass')
            
            acc = accuracies[j]
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                    f'{correct}/{total}\n({acc:.1f}%)', 
                    ha='center', va='bottom')
    
    plt.title('Model Performance by Method')
    plt.ylabel('Accuracy (%)')
    plt.xlabel('Model')
    plt.xticks(group_positions, [m.replace('_', ' ').upper() for m in models])
    
    # Adjust legend position to avoid overlapping
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Adjust layout to accommodate legend
    plt.tight_layout()
    
    # Create reports/assets directory if it doesn't exist
    os.makedirs('report/assets', exist_ok=True)
    plt.savefig('report/assets/accuracy_comparison.png', bbox_inches='tight')
    plt.close()
    
    return eval_results

def save_status_comparisons(eval_results):
    """Compare ReAct vs Voyager results and save differences to CSV"""
    for model in eval_results:
        # Compare ReAct vs Voyager
        status_groups = compare_dict_statuses(
            eval_results[model]['react'],
            eval_results[model]['voyager'],
            'react',
            'voyager'
        )
        
        # Save differences to CSV
        csv_path = f'report/assets/{model}_status_differences.csv'
        with open(csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['react_status', 'voyager_status', 'task_id'])
            
            for (s1, s2), task_ids in status_groups.items():
                if s1 != s2:  # Only save differences
                    for task_id in task_ids:
                        writer.writerow([s1, s2, task_id])

if __name__ == "__main__":
    eval_results = plot_accuracies()
    save_status_comparisons(eval_results)
