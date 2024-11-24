from collections import Counter

def find_duplicates(int_list):
    counts = Counter(int_list)
    duplicates = {num for (num, count) in counts.items() if (count > 1)}
    return duplicates
