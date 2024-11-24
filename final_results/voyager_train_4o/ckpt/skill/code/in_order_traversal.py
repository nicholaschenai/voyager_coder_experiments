

def in_order_traversal(tree):
    if (not tree):
        return []
    root = tree[0]
    left_subtree = (tree[1] if (len(tree) > 1) else [])
    right_subtree = (tree[2] if (len(tree) > 2) else [])
    return ((in_order_traversal(left_subtree) + [root]) + in_order_traversal(right_subtree))
