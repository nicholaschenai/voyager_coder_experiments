

def is_prime(n):
    if (n < 2):
        return False
    for i in range(2, (int((n ** 0.5)) + 1)):
        if ((n % i) == 0):
            return False
    return True




def sum_of_primes(numbers):
    total = 0
    for number in numbers:
        if is_prime(number):
            total += number
    return total
