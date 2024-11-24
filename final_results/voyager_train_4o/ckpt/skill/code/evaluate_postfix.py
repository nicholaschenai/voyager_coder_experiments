

def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if (token == '+'):
                result = (a + b)
            elif (token == '-'):
                result = (a - b)
            elif (token == '*'):
                result = (a * b)
            elif (token == '/'):
                result = int((a / b))
            stack.append(result)
    return stack.pop()
