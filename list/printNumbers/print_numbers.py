# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
#
#  示例 1:
#
#  输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
#
#
#
#
#  说明：
#
#
#  用返回一个整数列表来代替打印
#  n 为正整数
from typing import List


class Solution:
    def print_numbers(self, n: int) -> List[int]:
        max_num = 0
        for i in range(n-1, -1, -1):
            max_num += 9 * pow(10, i)
        return [i+1 for i in range(max_num)]

