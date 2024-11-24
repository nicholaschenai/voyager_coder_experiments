

def sum_of_multiples_of_6(int_list):
    total_sum = 0
    for number in int_list:
        if ((number % 6) == 0):
            total_sum += number
    return total_sum
