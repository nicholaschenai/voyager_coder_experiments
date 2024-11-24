

def sum_of_multiples_of_seven(int_list):
    total_sum = 0
    for num in int_list:
        if ((num % 7) == 0):
            total_sum += num
    return total_sum
