

def knapsack(items, max_weight):
    n = len(items)
    dp = [[0 for _ in range((max_weight + 1))] for _ in range((n + 1))]
    for i in range(1, (n + 1)):
        (weight, value) = items[(i - 1)]
        for w in range((max_weight + 1)):
            if (weight <= w):
                dp[i][w] = max(dp[(i - 1)][w], (dp[(i - 1)][(w - weight)] + value))
            else:
                dp[i][w] = dp[(i - 1)][w]
    return dp[n][max_weight]
