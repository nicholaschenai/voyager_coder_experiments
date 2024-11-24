

def climbing_stairs(n, memo=None):
    if (memo is None):
        memo = {}
    if (n == 0):
        return 1
    if (n < 0):
        return 0
    if (n in memo):
        return memo[n]
    memo[n] = ((climbing_stairs((n - 1), memo) + climbing_stairs((n - 2), memo)) + climbing_stairs((n - 3), memo))
    return memo[n]
