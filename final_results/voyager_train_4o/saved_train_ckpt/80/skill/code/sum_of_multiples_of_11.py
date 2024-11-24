

def sum_of_multiples_of_11(int_list):
    total_sum = 0
    for number in int_list:
        if ((number % 11) == 0):
            total_sum += number
    return total_sum
