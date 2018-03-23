'''
给定一个序列（至少含有 1 个数），从该序列中寻找一个连续的子序列，使得子序列的和最大。

例如，给定序列 [-2,1,-3,4,-1,2,1,-5,4]，
连续子序列 [4,-1,2,1] 的和最大，为 6。
'''

def maxSubArray(nums):
  maxSum = currSum = nums[0]
  for i in nums[1:]:
    currSum = max(i, currSum+i)
    maxSum = max(maxSum, currSum)
  return maxSum


if __name__ == '__main__':
  nums = [-2,1,-3,4,-1,2,1,-5,4]
  print(maxSubArray(nums))
