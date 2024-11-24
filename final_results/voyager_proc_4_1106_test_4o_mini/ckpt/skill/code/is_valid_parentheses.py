

def is_valid_parentheses(s: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if (char in bracket_map.values()):
            stack.append(char)
        elif (char in bracket_map):
            if ((not stack) or (stack[(- 1)] != bracket_map[char])):
                return False
            stack.pop()
    return (not stack)
