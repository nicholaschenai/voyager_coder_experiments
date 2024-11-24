

def sum_of_multiples(numbers):
    total_sum = 0
    for number in numbers:
        if (((number % 3) == 0) or ((number % 5) == 0)):
            total_sum += number
    return total_sum
