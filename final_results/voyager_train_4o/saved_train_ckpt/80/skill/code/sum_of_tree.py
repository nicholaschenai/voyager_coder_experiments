

def sum_of_tree(tree):
    if (not tree):
        return 0
    current_value = tree[0]
    left_sum = (sum_of_tree(tree[1]) if (len(tree) > 1) else 0)
    right_sum = (sum_of_tree(tree[2]) if (len(tree) > 2) else 0)
    return ((current_value + left_sum) + right_sum)
