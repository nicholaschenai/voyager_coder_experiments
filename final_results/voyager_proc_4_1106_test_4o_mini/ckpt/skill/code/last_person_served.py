from collections import deque

def last_person_served(ticket_numbers):
    queue = deque(ticket_numbers)
    while (len(queue) > 1):
        queue.popleft()
    return queue[0]
