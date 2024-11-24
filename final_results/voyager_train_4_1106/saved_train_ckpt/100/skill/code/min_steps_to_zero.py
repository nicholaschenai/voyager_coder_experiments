

def min_steps_to_zero(n):
    dp = ([0] * (n + 1))
    for i in range(1, (n + 1)):
        dp[i] = (dp[(i - 1)] + 1)
        if ((i % 2) == 0):
            dp[i] = min(dp[i], (dp[(i // 2)] + 1))
    return dp[n]
