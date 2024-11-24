

def look_and_say(n):
    if (n == 0):
        return '1'
    current_term = '1'
    for _ in range(1, n):
        next_term = ''
        count = 1
        for j in range(1, len(current_term)):
            if (current_term[j] == current_term[(j - 1)]):
                count += 1
            else:
                next_term += (str(count) + current_term[(j - 1)])
                count = 1
        next_term += (str(count) + current_term[(- 1)])
        current_term = next_term
    return current_term
