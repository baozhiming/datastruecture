#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A string字符串
# @return int整型
#
class Solution:
    max_length = -1
    def getLongestPalindrome(self, A: str) -> int:
        # write code here
        if not A:
            return 0
        if len(A) == 1:
            return 1
        for i in range(len(A)):
            end = len(A)
            if not self.is_palindrome(A[i:end]):
                self.getLongestPalindrome(A[i:end-1])
            if end - i + 1 > self.max_length:
                self.max_length = end -i + 1
        return self.max_length

    def is_palindrome(self, string: str) -> bool:
        begin, end = 0, len(string) - 1
        while begin < end:
            if string[begin].lower() != string[end].lower():
                return False
            begin += 1
            end -= 1
        return True
