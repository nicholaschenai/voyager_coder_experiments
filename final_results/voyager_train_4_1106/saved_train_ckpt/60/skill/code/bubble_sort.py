

def bubble_sort(input_list):
    n = len(input_list)
    for i in range((n - 1)):
        for j in range(((n - 1) - i)):
            if (input_list[j] > input_list[(j + 1)]):
                (input_list[j], input_list[(j + 1)]) = (input_list[(j + 1)], input_list[j])
    return input_list
