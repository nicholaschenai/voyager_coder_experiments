

def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total
