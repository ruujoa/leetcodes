'''
给定一个整数数列，找出其中和为特定值的那两个数。
你可以假设每个输入都只会有一种答案，同样的元素不能被重用。
示例:
  给定 nums = [2, 7, 11, 15], target = 9

  因为 nums[0] + nums[1] = 2 + 7 = 9
  所以返回 [0, 1]

The process of thinking listed below(6 functions, wrong to right)
'''

def twoSum_wrong1(nums, target):
  for i in nums:
    for j in nums[::-1]:
      if i + j == target:
        return [nums.index(i), nums.index(j)]

# case: nums = [3,2,4] target = 6, return [0, 0], expected [1, 2]

def twoSum_wrong2(nums, target):
  for i in nums:
    for j in nums[1:]:
      if i + j == target:
        return [nums.index(i), nums.index(j)]
# case: nums = [3,3] target = 6, return [0, 0], expected [0, 1]

def twoSum_wrong3(nums, target):
  for i in nums:
    for j in nums[1:]:
      if i + j == target:
        return [nums.index(i), nums[1:].index(j)]

# case: nums = [3,3] target = 6, return [0, 0], expected [0, 1]

def twoSum_wrong4(nums, target):
  for i in nums:
    for j in nums[1:]:
      if i + j == target:
        return [nums.index(i), nums[1:].index(j)+1]

# case: nums = [2,5,5,11] target = 10, return [1, 1], expected [1, 2]


def twoSum_wrong5(nums, target):
  numc = nums
  for i in nums:
    for j in numc:
      if i + j == target and nums.index(i) != numc.index(j):
        return [nums.index(i), numc.index(j)]

# case: nums = [2,5,5,11] target = 10, return None, expected [1, 2]

# right: Time complexity -> O(n²)
def twoSum1(nums, target):
  numc = nums
  for i,j in enumerate(nums):
    for a,b in enumerate(numc):
      if j+b == target and i != a:
        return [i, a]

# right: Time complexity -> O(n)
def twoSum2(nums, target):
  dict = {}
  for i,j in enumerate(nums):
    complement = target - j
    if complement in dict.keys():
      return [dict[complement], i]
    dict[j] = i


if __name__ == '__main__':
  nums = [2,5,5,11]
  print(twoSum2(nums, 10))
