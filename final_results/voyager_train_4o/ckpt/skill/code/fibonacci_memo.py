

def fibonacci_memo(n, memo={}):
    if (n in memo):
        return memo[n]
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    memo[n] = (fibonacci_memo((n - 1), memo) + fibonacci_memo((n - 2), memo))
    return memo[n]
