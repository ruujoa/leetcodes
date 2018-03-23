'''
假设有一个数组，它的第 i 个元素是一个给定的股票在第 i 天的价格。

设计一个算法来找到最大的利润。你可以完成尽可能多的交易（多次买卖股票）。然而，你不能同时参与多个交易（你必须在再次购买前出售股票）。
'''
def maxProfit(prices):
  return sum(max(prices[i] - prices[i-1], 0) for i in range(1, len(prices)))

if __name__ == '__main__':
  prices1 = [7, 1, 5, 3, 6, 4]
  print(maxProfit(prices1))
