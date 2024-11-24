

def evaluate_expression(expression):
    result = 0
    current_number = 0
    current_operator = '+'
    for char in expression:
        if char.isdigit():
            current_number = ((current_number * 10) + int(char))
        else:
            if (current_operator == '+'):
                result += current_number
            elif (current_operator == '-'):
                result -= current_number
            current_operator = char
            current_number = 0
    if (current_operator == '+'):
        result += current_number
    elif (current_operator == '-'):
        result -= current_number
    return result
