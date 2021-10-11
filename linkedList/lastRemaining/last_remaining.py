"""
约瑟夫问题：0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
"""


class Solution:
    def last_remaining(self, n: int, m: int) -> int:
        return self.find_m(n, m)

    def find_m(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        x = self.find_m(n-1, m)
        return ((m % n) + x) % n
