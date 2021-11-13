"""
求一个非负数的平方根，精确度为小数点后六位
"""
from decimal import Decimal


class Solution:
    def sqrt(self, num: int) -> float:
        if num == 0:
            return num
        left = 1 if num % 2 == 1 else 0
        right = num
        middle = left + (right - left) / 2.0
        while abs(middle * middle - num) > 0.000001:
            if middle * middle > num:
                right = middle
                middle = left + (right - left) / 2.0
            elif middle * middle < num:
                left = middle
                middle = left + (right - left) / 2.0
        return middle


"""
使用二分法，middle的平方与原值比较。中止条件为middle^2 - x的绝对值小于等于0。000001
"""