

def sum_of_squares_of_evens(numbers):
    total_sum = 0
    for number in numbers:
        if ((number % 2) == 0):
            total_sum += (number ** 2)
    return total_sum
