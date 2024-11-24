

def sum_of_two_largest(numbers):
    largest = find_kth_largest(numbers, 1)
    second_largest = find_kth_largest(numbers, 2)
    return (largest + second_largest)
