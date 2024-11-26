# An analysis of Voyager for coding tasks

## About
This repo contains experiments with the Voyager agent for coding tasks.

Reference: "Voyager: An Open-Ended Embodied Agent with Large Language Models" by
Wang et. al. (2023) https://github.com/MineDojo/Voyager

The report can be found [here](report/README.md)

## Installation

### Setup Instructions
1. Clone the repository with submodules:
```bash
git clone --recursive https://github.com/nicholaschenai/voyager_coder_experiments.git
cd voyager_coder_experiments
```

2. Create and activate the conda environment using the provided environment.yml:
```bash
conda env create -f environment.yml
conda activate voyager_coder
```

3. Set up API keys as described below

## Reproducing experiments
### Set API keys
For OpenAI:
```bash
export OPENAI_API_KEY="YOUR_KEY_HERE"
```

Azure OpenAI:
```bash
export AZURE_OPENAI_API_KEY="YOUR_KEY_HERE"
export AZURE_OPENAI_ENDPOINT="ENDPOINT_URL_HERE"
export OPENAI_API_VERSION="2023-07-01-preview"
export AZURE_OPENAI_DEPLOYMENT_NAME="{'gpt-4-1106-preview': 'YOUR_DEPLOYMENT_NAME_HERE', 'gpt-4o-mini-2024-07-18': 'YOUR_DEPLOYMENT_NAME_HERE'}"
```

### Run scripts
#### ReAct
GPT-4o-mini:
```bash
bash scripts/react_test_4o_mini.sh
```

GPT-4-1106:
```bash
bash scripts/react_test_4_1106.sh
```

#### Voyager

First run training to get the skills library:
```bash
bash scripts/voyager_train_4_1106.sh
```

Then proceed to use the skills library for evaluation:
GPT-4-1106:
```bash
bash scripts/voyager_proc_4_1106_test_4_1106.sh
```

GPT-4o-mini:
```bash
bash scripts/voyager_proc_4_1106_test_4o_mini.sh
```

### Data analysis
Plot accuracies, get error analysis:
```bash
python scripts/results_analysis.py
```

To check for multi-function solutions:
```bash
python scripts/find_multi_fn_solns.py
```

### Data outputs
Experiment outputs will be saved in the following locations:
- Logs: `logs/`
- Results: `results/`

Example structure of a result folder (e.g. `voyager_proc_4_1106_test_4_1106/`):
```
voyager_proc_4_1106_test_4_1106/
├── args.json                  # Experiment configuration and hyperparameters
├── samples_eval_results.json # MBPP Plus evaluation results
├── samples.jsonl              # Agent output used for evaluation
├── result_dict.json            # Public test case execution result
├── ckpt/                      # Checkpoint directory containing:
│   ├── curriculum/            # QA db, completed and failed tasks
│   └── skill/                 # Learned skills in code, description and vectordb
├── test_outputs/              # logs and final output per problem
```

Accuracy plot saved in `report/assets/accuracy_comparison.png`
Error analysis saved in `report/assets/4o_mini_status_differences.csv` and `report/assets/4_1106_status_differences.csv`

## Project Structure
```
.
├── cognitive_base/      # Cognitive architecture primitives
├── agent_expt_suite/    # tools for running experiments with agents
├── voyager_coder/       # Voyager agent architecture for coding tasks
├── scripts/            # Running scripts
├── report/             # Documentation and analysis
└── final_results/      # Experiment outputs
```


## License
TODO