'''
判断一个整数是否是回文数。不能使用辅助空间。

点击查看提示

一些提示:

负整数可以是回文数吗？（例如 -1）

如果你打算把整数转为字符串，请注意不允许使用辅助空间的限制。

你也可以考虑将数字颠倒。但是如果你已经解决了 “颠倒整数” 问题的话，就会注意到颠倒整数时可能会发生溢出。你怎么来解决这个问题呢？

本题有一种比较通用的解决方式。
'''
def isPalindrome_poor(num):
  return str(num)[:] == str(num)[::-1] # 粗暴解法，没有考虑溢出问题，而且不符合“不能使用辅助空间”的限制

def isPalindrome(num):
  if num < 0 or (num % 10 == 0 and num != 0):
    return False
  rev = 0
  while num > rev:
    rev = rev * 10 + num % 10
    num //= 10

  return num == rev or num == rev // 10

if __name__ == '__main__':
  print(isPalindrome(122321))
