

def filter_prime_numbers(int_list):

    def is_prime(n):
        if (n <= 1):
            return False
        for i in range(2, (int((n ** 0.5)) + 1)):
            if ((n % i) == 0):
                return False
        return True
    prime_list = [num for num in int_list if is_prime(num)]
    return prime_list
