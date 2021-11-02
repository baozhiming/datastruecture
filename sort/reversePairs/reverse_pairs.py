"""
求数组中逆序对的个数
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
"""
from typing import List


class Solution:
    def reverse_pairs(self, nums: List) -> int:
        return self.__merge_sort(nums, 0, len(nums) - 1)

    def __merge_sort(self, nums: List, left: int, right: int) -> int:
        if left >= right:
            return 0
        middle = left + int((right - left) / 2)
        a = self.__merge_sort(nums, left, middle)
        b = self.__merge_sort(nums, middle+1, right)
        return a + b + self.__merge(nums, left, middle, right)

    def __merge(self, nums: List, left: int, middle: int, right: int) -> int:
        pre, last = left, middle+1
        tmp_nums = []
        reverse_pairs = 0
        while pre <= middle and last <= right:
            if nums[pre] <= nums[last]:
                tmp_nums.append(nums[pre])
                pre += 1
            else:
                tmp_nums.append(nums[last])
                last += 1
                reverse_pairs += middle - pre + 1
        while pre <= middle:
            tmp_nums.append(nums[pre])
            pre += 1
        while last <= right:
            tmp_nums.append(nums[last])
            last += 1
        nums[left:right+1] = tmp_nums
        return reverse_pairs



if __name__ == "__main__":
    nums = [7, 5, 6, 4]
    solution = Solution()
    re = solution.reverse_pairs(nums)
    assert re == 5




"""
思路：使用暴力解法，两次遍历获取逆序对。时间复杂度为n的平方。
考虑完全逆序的数组：5，4，3，2，1 。不需要计算，便可知道和5构成逆序对的有4个。和4构成逆序对的有3个。如果数组有序，则可O1时间获取
逆序对个数。
归并排序。在合并的时候，有两个已经排序好的数组。在合并装入一个数组，并且后面数组的第一个元素小于前面数组的第一个元素，
此时第一个数组的所有元素都可以和后一个数组的第一个元素构成逆序对。
时间复杂度：nlogn
空间复杂度为n
是稳定的排序算法。
"""
