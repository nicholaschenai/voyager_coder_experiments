

def sum_of_smallest(numbers):
    if (len(numbers) < 2):
        raise ValueError('List must contain at least two integers.')
    smallest = float('inf')
    second_smallest = float('inf')
    for number in numbers:
        if (number < smallest):
            second_smallest = smallest
            smallest = number
        elif (number < second_smallest):
            second_smallest = number
    return (smallest + second_smallest)
