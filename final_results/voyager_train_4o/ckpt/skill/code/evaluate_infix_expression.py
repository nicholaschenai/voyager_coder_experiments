import re

def tokenize(expression):
    import re
    tokens = re.findall('\\d+|[+*/()-]', expression)
    return tokens




def precedence(op):
    if (op in ('+', '-')):
        return 1
    if (op in ('*', '/')):
        return 2
    return 0




def apply_operator(operands, operator):
    b = operands.pop()
    a = operands.pop()
    if (operator == '+'):
        operands.append((a + b))
    elif (operator == '-'):
        operands.append((a - b))
    elif (operator == '*'):
        operands.append((a * b))
    elif (operator == '/'):
        operands.append(int((a / b)))




def evaluate_infix_expression(expression):
    tokens = tokenize(expression)
    num_stack = []
    op_stack = []
    for token in tokens:
        if token.isdigit():
            num_stack.append(int(token))
        elif (token in '+-*/'):
            while (op_stack and (precedence(op_stack[(- 1)]) >= precedence(token))):
                apply_operator(num_stack, op_stack.pop())
            op_stack.append(token)
        elif (token == '('):
            op_stack.append(token)
        elif (token == ')'):
            while (op_stack and (op_stack[(- 1)] != '(')):
                apply_operator(num_stack, op_stack.pop())
            op_stack.pop()
    while op_stack:
        apply_operator(num_stack, op_stack.pop())
    return num_stack[0]
