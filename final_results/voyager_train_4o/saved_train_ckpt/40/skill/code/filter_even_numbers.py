

def filter_even_numbers(input_list):
    even_numbers = []
    for number in input_list:
        if ((number % 2) == 0):
            even_numbers.append(number)
    return even_numbers
