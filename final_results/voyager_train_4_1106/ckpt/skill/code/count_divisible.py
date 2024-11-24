

def count_divisible(int_list, divisor):
    if (divisor == 0):
        raise ValueError('Divisor cannot be zero.')
    count = 0
    for number in int_list:
        if (((number != 0) or (divisor > 0)) and ((number % divisor) == 0)):
            count += 1
    return count
