

def calculate_expression(expression):
    numbers = expression.split('+')
    integers = map(int, numbers)
    return sum(integers)
