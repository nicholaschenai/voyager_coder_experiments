

def min_coins_for_change(denominations, target):
    dp = ([float('inf')] * (target + 1))
    dp[0] = 0
    for coin in denominations:
        for amount in range(coin, (target + 1)):
            dp[amount] = min(dp[amount], (dp[(amount - coin)] + 1))
    return (dp[target] if (dp[target] != float('inf')) else (- 1))
