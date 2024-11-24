

def first_repeated_integer(int_list):
    seen = {}
    for num in int_list:
        if (num in seen):
            return num
        seen[num] = True
    return None
