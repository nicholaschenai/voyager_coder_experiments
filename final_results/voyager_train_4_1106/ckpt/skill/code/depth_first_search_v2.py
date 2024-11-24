

def depth_first_search(graph):
    visited_order = []
    visited = set()

    def dfs_helper(node):
        if (node not in visited):
            visited.add(node)
            visited_order.append(node)
            for neighbor in graph[node]:
                dfs_helper(neighbor)
    for node in graph:
        if (node not in visited):
            dfs_helper(node)
    return visited_order
