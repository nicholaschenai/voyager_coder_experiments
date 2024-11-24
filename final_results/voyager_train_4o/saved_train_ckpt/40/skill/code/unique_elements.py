from collections import Counter

def unique_elements(input_list):
    counts = Counter(input_list)
    unique_integers = [num for (num, count) in counts.items() if (count == 1)]
    unique_integers.sort()
    return unique_integers
