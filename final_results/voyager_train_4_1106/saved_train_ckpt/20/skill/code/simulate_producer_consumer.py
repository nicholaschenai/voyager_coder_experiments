

def simulate_producer_consumer(items):
    queue = []
    consumed_count = 0
    for item in items:
        queue.append(item)
    while queue:
        item = queue.pop(0)
        print(item)
        consumed_count += 1
    return consumed_count
