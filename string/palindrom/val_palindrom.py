# 获取最长的回文子串
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A string字符串
# @return int整型
#
class Solution:
    def getLongestPalindrome(self, A: str) -> int:
        # write code here
        if not A:
            return 0
        max_len = 1
        for i in range(len(A)):
            pre, last = i - 1, i + 1
            while pre >= 0 and last < len(A) and A[pre] == A[last]:
                if last - pre + 1 > max_len:
                    max_len = last - pre + 1
                pre -= 1
                last += 1
        for i in range(len(A)):
            pre, last = i, i + 1
            while pre >=0 and last < len(A) and A[pre] == A[last]:
                if last - pre + 1 > max_len:
                    max_len = last - pre + 1
                pre -= 1
                last += 1
        return max_len

handler = Solution()
print(handler.getLongestPalindrome("abbba"))



"""
-1：暴力解法
1。 使用了中心扩散法
2。 动态规划：使用的思路是写出动态规划方程式，方程式则是根据暴力接发获取到的规律.状态转移表。
3。 时间复杂度为n的算法。结合了预处理+中心扩散+动态规划。很复杂
使用#对字符进行预处理，扩展n倍，使其变成奇数。
预处理之后的最大回文子串长度为：preprocess_max_len，实际字符串的最大回文长度为 max_len ，则(preprocess_max_len - 1) /2 = max_len
使用如下变量：
i: 循环遍历
rightest_index: 目前为止最大回文子串的最右边的索引
center：最大回文子串的中心点
mirror: 当前i对应center的对称点
states：动态规划的状态转移表。每个元素记录每个索引对应位置的最大回文子串的长度 - 1 / 2。
分类：
1> i >= rightest_index:
      中心扩散法
2> i < rightest_index:
      a> states[mirror] < rightest_index - i:
          states[i] = states[mirror]
      b> states[mirror] = rightest_index - i:
          states[i] = states[mirror] + 中心扩散 
      c> states[mirror] > rightest_index - i:
          states[i] = rightest_index - i
"""