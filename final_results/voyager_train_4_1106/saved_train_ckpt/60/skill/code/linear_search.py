

def linear_search(int_list, target):
    for (index, value) in enumerate(int_list):
        if (value == target):
            return index
    return (- 1)
