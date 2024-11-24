

def sort_strings_by_vowel_count(strings):

    def count_vowels(s):
        return sum((1 for char in s.lower() if (char in 'aeiou')))
    sorted_strings = sorted(strings, key=(lambda s: ((- count_vowels(s)), s)))
    return sorted_strings
