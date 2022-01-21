"""
打印全排列
"""
from typing import List


class Solution:
    def print_permutation(self, nums: List, n: int, k: int):
        """

        :param nums: 全排列的数字
        :param n: 数组的大小
        :param k: 全排列子数组的大小
        :return:
        """
        if k == 1:
            print(" ".join([str(i) for i in nums]))
            print("\n")

        for i in range(k):
            tmp = nums[i]
            nums[i] = nums[k - 1]
            nums[k - 1] = tmp

            self.print_permutation(nums, n, k -1)

            tmp = nums[i]
            nums[i] = nums[k - 1]
            nums[k - 1] = tmp


handler = Solution()
handler.print_permutation([1, 2, 3, 4], 4, 4)