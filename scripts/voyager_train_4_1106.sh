small_model="gpt-4o-mini-2024-07-18"
# large_model="gpt-4o-2024-08-06"
large_model="gpt-4-1106-preview"
result_dir="results/voyager_train_4_1106"

python main.py \
--do_train \
--resume \
--result_dir $result_dir \
--qa_model_name $small_model \
--desc_model_name $small_model \
--agent_type voyager \
--verbose \
--max_display_tests 10 --max_display_chars 1000 \
--model_name $large_model \
--max_train_iter 100 \
--save_every 20
