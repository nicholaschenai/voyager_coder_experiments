

def depth_first_search(graph, start):
    visited_order = []
    visited = set()

    def dfs_helper(node):
        if (node not in visited):
            visited.add(node)
            visited_order.append(node)
            for neighbor in graph[node]:
                dfs_helper(neighbor)
    dfs_helper(start)
    return visited_order
