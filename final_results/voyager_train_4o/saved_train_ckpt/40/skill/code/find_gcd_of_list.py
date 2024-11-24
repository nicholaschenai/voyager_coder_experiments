

def gcd(a, b):
    while (b != 0):
        (a, b) = (b, (a % b))
    return a




def find_gcd_of_list(numbers):
    if (not numbers):
        return None
    current_gcd = numbers[0]
    for num in numbers[1:]:
        current_gcd = gcd(current_gcd, num)
    return current_gcd
