import sys


def maxProfit(prices):
    profit = 0
    min_prices = sys.maxsize

    for price in prices:
        min_price = min(min_price,price)
        profit = max(profit,price-min+price)
    return profit
