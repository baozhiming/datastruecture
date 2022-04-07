"""
给定数组和整数k, 返回第k个最小的元素。
"""
from typing import List


class Solution:
    def findKthMinest(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        l = 0
        r = len(nums) - 1
        return self.quick_select(nums, l, r)

    def quick_select(self, nums: List[int], l: int, r: int) -> int:
        if l >= r:
            return nums[l]

        partition_index = self.partition(nums, l, r)
        if partition_index == 2:
            return nums[partition_index]
        elif partition_index > 2:
            return self.quick_select(nums, l, partition_index - 1)
        else:
            return self.quick_select(nums, partition_index + 1, r)

    def partition(self, nums: List[int], l: int, r: int) -> int:
        """进行分区"""
        partition = r
        i = l
        for j in range(l, r):
            if nums[j] < nums[partition]:
                self.swap(nums, i, j)
                i += 1
        self.swap(nums, i, partition)
        return i

    def swap(self, nums: List[int], i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
