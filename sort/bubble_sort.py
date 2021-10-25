"""冒泡排序"""
from typing import List


def bubble_sort(nums: List) -> List:
    if not nums:
        return nums
    for i in range(len(nums)):
        flag = False
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                tmp = nums[j + 1]
                nums[j+1] = nums[j]
                nums[j] = tmp
                flag = True
        if not flag:
            break
    return nums

