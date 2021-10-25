"""
两个没有重复元素的数组，nums1和nums2。nums1是nums2的子集
找出nums1中每个元素在nums2中右边比他大的第一个元素。
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map_ = {}
        for i in nums2:
            if len(stack) == 0 or i <= stack[-1]:
                stack.append(i)
            else:
                while len(stack) > 0 and i > stack[-1]:
                    map_[stack.pop()] = i
                stack.append(i)
        while len(stack) > 0:
            map_[stack.pop()] = -1

        re = []
        for i in nums1:
            re.append(map_[i])
        return re


"""
思路：
暴力解法：迭代nums1中的每个元素。定位元素在nums2中的位置，找到右边最大的值
时间复杂度为：O（N * M）
空间复杂度：O（N）
优化解法：
思路：空间换时间的思路，模式识别：找到右边第一个比自己大的元素元素是典型的栈的应用。先找到nums2中每个元素的
"""