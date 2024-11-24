

def simulate_stack_operations(operations):
    stack = []
    results = []
    for operation in operations:
        if operation.startswith('push'):
            (_, value) = operation.split()
            stack.append(int(value))
        elif (operation == 'pop'):
            if stack:
                results.append(stack.pop())
            else:
                results.append(None)
        elif (operation == 'peek'):
            if stack:
                results.append(stack[(- 1)])
            else:
                results.append(None)
    return results
