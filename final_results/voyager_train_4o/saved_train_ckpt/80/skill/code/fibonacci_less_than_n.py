

def fibonacci_less_than_n(n):
    fib_list = []
    (a, b) = (0, 1)
    while (a < n):
        fib_list.append(a)
        (a, b) = (b, (a + b))
    return fib_list
