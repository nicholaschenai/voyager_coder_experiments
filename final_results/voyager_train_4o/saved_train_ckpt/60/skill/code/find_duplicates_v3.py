

def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    for number in input_list:
        if (number in seen):
            duplicates.add(number)
        else:
            seen.add(number)
    return sorted(duplicates)
