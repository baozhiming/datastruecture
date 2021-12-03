"""
返回字符中第一个只出现一次的字符
s = "adabdccehs"
"""
from typing import Dict


class Solution:
    def first_uniq_char(self, s: str) -> str:
        char2count: Dict = {}
        for i in s:
            if i in char2count:
                char2count[i] += 1
            else:
                char2count[i] = 1
        for i in s:
            if char2count[i] == 1:
                return i
        return ' '


"""
思路：这道题时数组引出的。数组支持随机访问，根据O(1)时间的随机访问这个特性，可以轻松的实现散列表。进而引出了此题。
这道题的暴力解法需要n^2的时间复杂度。
利用散列表，key为字符，value为每个字符出现的次数。顺序遍历字符串，直到找到value为1的字符。
"""