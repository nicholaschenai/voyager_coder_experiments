

def find_nth_prime(n):
    if (n < 1):
        raise ValueError('There is no such thing as the 0th prime or negative prime numbers.')
    primes = [2]
    num = 2
    while (len(primes) < n):
        num += 1
        for prime in primes:
            if (prime > int((num ** 0.5))):
                primes.append(num)
                break
            if ((num % prime) == 0):
                break
        else:
            primes.append(num)
    return primes[(- 1)]
