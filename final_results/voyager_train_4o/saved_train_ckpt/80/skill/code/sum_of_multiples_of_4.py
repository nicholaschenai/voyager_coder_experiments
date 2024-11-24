

def sum_of_multiples_of_4(numbers):
    total = 0
    for number in numbers:
        if ((number % 4) == 0):
            total += number
    return total
