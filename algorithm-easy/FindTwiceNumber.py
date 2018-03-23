'''
在一个给定的数组nums中，总是存在一个最大元素 。
查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
如果是，则返回最大元素的索引，否则返回-1。

示例 1:
输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.

示例 2:
输入: nums = [1, 2, 3, 4]
输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.
'''

def dominantIndex(nums):
  if all((max(nums) // x >= 2 for x in nums if x > 0 and x!=max(nums))):
    return nums.index(max(nums))
  else:
    return -1

if __name__ == '__main__':
  nums1 = [3, 6, 1, 0]
  print(dominantIndex(nums1))
  nums2 = [1, 2, 3, 4]
  print(dominantIndex(nums2))
