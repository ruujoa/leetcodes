import sys

'''
给定一个索引 k，返回帕斯卡三角形（杨辉三角）的第 k 行。
例如，给定 k = 3，
则返回 [1, 3, 3, 1]。

注：
你可以优化你的算法到 O(k) 的空间复杂度吗？
'''
def getRow(rowIndex):
  row = [1]
  for _ in range(rowIndex):
    row = [x + y for x, y in zip([0]+row, row+[0])]
  return row

'''
给定 numRows, 生成帕斯卡三角形的前 numRows 行。
例如, 给定 numRows = 5,
返回
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
def generate(numRows):
  if numRows == 0:
    return []
  row = [1]
  list = [[1]]
  for _ in range(numRows-1):
    row = [x + y for x, y in zip([0]+row, row+[0])]
    list.append(row)
  return list

if __name__ == '__main__':
  index = int(sys.argv[1])
  l = getRow(index)
  print(l)
  ll = generate(index)
  print(ll)
