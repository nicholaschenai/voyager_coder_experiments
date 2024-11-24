

def cumulative_sum(input_list):
    cumulative_sum = 0
    cumulative_list = []
    for number in input_list:
        cumulative_sum += number
        cumulative_list.append(cumulative_sum)
    return cumulative_list
