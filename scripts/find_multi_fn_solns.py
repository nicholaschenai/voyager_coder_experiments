"""
find those that have multiple functions, in case compositionality by copying skills instead of calling them
"""
from pathlib import Path

from cognitive_base.utils import load_json
from voyager_coder.utils.code_parse import extract_from_ast

def find_multi_fns(base_dir="final_results/voyager_train_4_1106/train_outputs"):
    base_path = Path(base_dir)
    
    # Loop through all numbered directories in train_outputs
    for output_dir in sorted(base_path.glob("*")):
        if not output_dir.is_dir():
            continue
            
        output_file = output_dir / "output.json"
        if not output_file.exists():
            continue
            
        try:
            data = load_json(output_file)
            # print(f"\n=== Output from {output_dir.name} ===")
            full_code = data.get("full_code", "")
            if full_code:
                functions, _, _, _ = extract_from_ast(full_code)
                if len(functions) > 1:
                    print(f"Multiple functions found in {output_dir.name}")
        except Exception as e:
            print(f"Error processing {output_file}: {e}")
    print("\n\n")

if __name__ == "__main__":
    find_multi_fns()
    find_multi_fns("final_results/voyager_proc_4_1106_test_4_1106/test_outputs")
    find_multi_fns("final_results/voyager_proc_4_1106_test_4o_mini/test_outputs")

# Voyager train
# Multiple functions found in 13
# Multiple functions found in 32
# Multiple functions found in 33
# Multiple functions found in 64
# Multiple functions found in 70
# Multiple functions found in 83
# Multiple functions found in 92
# Multiple functions found in 93

# voyager test 4 1106
# Multiple functions found in Mbpp_100
# Multiple functions found in Mbpp_123
# Multiple functions found in Mbpp_141
# Multiple functions found in Mbpp_160
# Multiple functions found in Mbpp_223
# Multiple functions found in Mbpp_256
# Multiple functions found in Mbpp_260
# Multiple functions found in Mbpp_274
# Multiple functions found in Mbpp_286
# Multiple functions found in Mbpp_296
# Multiple functions found in Mbpp_462
# Multiple functions found in Mbpp_472
# Multiple functions found in Mbpp_57
# Multiple functions found in Mbpp_583
# Multiple functions found in Mbpp_592
# Multiple functions found in Mbpp_635
# Multiple functions found in Mbpp_765


# voyager test 4o mini
# Multiple functions found in Mbpp_100
# Multiple functions found in Mbpp_123
# Multiple functions found in Mbpp_141
# Multiple functions found in Mbpp_160
# Multiple functions found in Mbpp_256
# Multiple functions found in Mbpp_260
# Multiple functions found in Mbpp_296
# Multiple functions found in Mbpp_395
# Multiple functions found in Mbpp_456
# Multiple functions found in Mbpp_462
# Multiple functions found in Mbpp_583
# Multiple functions found in Mbpp_603
# Multiple functions found in Mbpp_635
