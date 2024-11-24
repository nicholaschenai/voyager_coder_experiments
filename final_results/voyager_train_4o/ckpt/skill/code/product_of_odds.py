

def product_of_odds(numbers):
    product = 1
    for number in numbers:
        if ((number % 2) != 0):
            product *= number
    return product
