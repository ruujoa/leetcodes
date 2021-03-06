'''
假设你有一个数组，其中第 i 个元素是一支给定股票第 i 天的价格。

如果您只能完成最多一笔交易（即买入和卖出一股股票），则设计一个算法来找到最大的利润。

示例 1:

输入: [7, 1, 5, 3, 6, 4]
输出: 5

最大利润 = 6-1 = 5（不是 7-1 = 6, 因为卖出价格需要大于买入价格）


示例 2:

输入: [7, 6, 4, 3, 1]
输出: 0

在这种情况下, 没有交易完成, 即最大利润为 0。
'''

def maxProfit(prices):
  max_profit, min_price = 0, float('inf')
  for price in prices:
    min_price = min(price, min_price)
    profit = price - min_price
    max_profit = max(profit, max_profit)
  return max_profit

if __name__ == '__main__':
  prices1 = [7, 1, 5, 3, 6, 4]
  print(maxProfit(prices1))
  prices2 = [7, 6, 4, 3, 1]
  print(maxProfit(prices2))
