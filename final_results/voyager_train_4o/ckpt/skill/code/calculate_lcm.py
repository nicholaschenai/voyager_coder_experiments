from functools import reduce

def gcd(a, b):
    while (b != 0):
        (a, b) = (b, (a % b))
    return a




def lcm(a, b):
    return (abs((a * b)) // gcd(a, b))




def calculate_lcm(numbers):
    if (not numbers):
        return None
    return reduce(lcm, numbers)
