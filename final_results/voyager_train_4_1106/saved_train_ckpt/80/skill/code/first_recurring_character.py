

def first_recurring_character(int_list):
    seen = set()
    for num in int_list:
        if (num in seen):
            return num
        seen.add(num)
    return None
