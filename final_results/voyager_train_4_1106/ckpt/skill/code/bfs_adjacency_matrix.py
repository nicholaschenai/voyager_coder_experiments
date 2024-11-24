from collections import deque

def bfs_adjacency_matrix(adj_matrix):
    visited = set()
    queue = deque([0])
    visited.add(0)
    visited_order = []
    while queue:
        current_node = queue.popleft()
        visited_order.append(current_node)
        for (neighbor, is_connected) in enumerate(adj_matrix[current_node]):
            if (is_connected and (neighbor not in visited)):
                visited.add(neighbor)
                queue.append(neighbor)
    return visited_order
