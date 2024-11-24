

def sum_of_multiples_of_13(int_list):
    total_sum = 0
    for number in int_list:
        if ((number % 13) == 0):
            total_sum += number
    return total_sum
