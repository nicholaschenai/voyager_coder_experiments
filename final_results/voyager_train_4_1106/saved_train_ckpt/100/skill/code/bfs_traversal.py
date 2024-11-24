from collections import deque

def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order_of_visit = []
    while queue:
        current_node = queue.popleft()
        order_of_visit.append(current_node)
        for neighbor in graph[current_node]:
            if (neighbor not in visited):
                visited.add(neighbor)
                queue.append(neighbor)
    return order_of_visit
