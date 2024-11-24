

def sum_of_odds(numbers):
    total = 0
    for number in numbers:
        if ((number % 2) != 0):
            total += number
    return total
