# ReAct, basically Voyager without skill library
small_model="gpt-4o-mini-2024-07-18"
# large_model="gpt-4o-2024-08-06"
large_model="gpt-4-1106-preview"
result_dir="results/react_test_4_1106"

python main.py \
--test_dataset_name MBPP_Plus \
--do_test --eval_later --use_public_tests \
--resume \
--result_dir $result_dir \
--qa_model_name $small_model \
--desc_model_name $small_model \
--agent_type voyager \
--verbose \
--max_display_tests 10 --max_display_chars 1000 \
--model_name $large_model

evalplus.evaluate --dataset mbpp --samples "${result_dir}/samples.jsonl"