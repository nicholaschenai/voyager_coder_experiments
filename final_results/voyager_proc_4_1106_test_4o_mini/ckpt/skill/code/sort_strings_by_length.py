

def sort_strings_by_length(strings):
    return sorted(strings, key=(lambda s: ((- len(s)), s)))
