"""
给定数组和整数k, 返回第k个最大的元素。
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k > len(nums):
            return -1

        l = 0
        r = len(nums) - 1
        return self.quick_select(nums, l, r, k)

    def quick_select(self, nums: List[int], l: int, r: int, k: int) -> int:
        if l >= r:
            return nums[l]

        partition_index = self.partition(nums, l, r)
        if len(nums) - partition_index == k:
            return nums[partition_index]
        elif len(nums) - partition_index > k:
            return self.quick_select(nums, partition_index + 1, r, k)
        else:
            return self.quick_select(nums, l, partition_index - 1, k)

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

# """
# 思路：最笨的方法是先排序，在随机访问。即使使用快排，时间复杂度也为 n log n。
#      在快速排序时，每轮递归都会根据分区点，将数组分为大于分区点和小于分区点两部分。而分区点则位于数组中正确的位置，如果是升序，分区点的索引为i，
#      则分区点位于第i+1小的元素。利用这个思想，可以每次递归讲述组分区，分区之后将分区点和k比较，对一半进行递归查找。这个思想也就是快速选择算法。
# 时间复杂度：最好时间复杂度为O(n)，最坏时间复杂度为O（n^2），平均时间复杂度为O(n),此处在算法导论上有一大快为证明。
# 空间复杂度：O（1）原地算法
# """
