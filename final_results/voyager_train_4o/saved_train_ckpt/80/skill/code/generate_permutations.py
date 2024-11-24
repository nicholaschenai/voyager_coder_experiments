from itertools import permutations

def generate_permutations(int_list):
    return [list(p) for p in permutations(int_list)]
