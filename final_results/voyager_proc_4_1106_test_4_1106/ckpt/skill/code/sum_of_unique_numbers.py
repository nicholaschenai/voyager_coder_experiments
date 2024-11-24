

def sum_of_unique_numbers(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = (frequency.get(num, 0) + 1)
    unique_sum = sum((num for (num, count) in frequency.items() if (count == 1)))
    return unique_sum
