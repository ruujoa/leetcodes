'''
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。
'''

def containsDuplicate(nums):
  counter = {}
  for i in nums:
    if i in counter.keys():
      return True
    else:
      counter.update({i:1})
  return False

if __name__ == '__main__':
  nums1 = [7, 2, 3, 2, 4, 6, 8]
  print(containsDuplicate(nums1))
  nums2 = [7, 2, 3, 1, 4, 6, 8]
  print(containsDuplicate(nums2))
