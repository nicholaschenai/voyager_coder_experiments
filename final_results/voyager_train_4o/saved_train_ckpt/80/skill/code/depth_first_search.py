

def depth_first_search(graph, start):
    visited = set()
    result = []

    def dfs_helper(node):
        if (node not in visited):
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                dfs_helper(neighbor)
    dfs_helper(start)
    return result
