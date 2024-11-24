from collections import Counter

def find_duplicates(input_list):
    counts = Counter(input_list)
    duplicates = {num for (num, count) in counts.items() if (count > 1)}
    return sorted(duplicates)
