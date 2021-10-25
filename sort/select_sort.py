"""选择排序"""
from typing import List


def select_sort(nums: List) -> List:
    if not nums or len(nums) == 1:
        return nums
    for i in range(0, len(nums)):
        min_value = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_value]:
                min_value = j
        if i != min_value:
            tmp = nums[min_value]
            nums[min_value] = nums[i]
            nums[i] = tmp
    return nums
