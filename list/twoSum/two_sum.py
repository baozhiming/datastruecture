"""
给一个递增的数组，和一个数字s，返回两个数字中的元素，和为s
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return []
        slow, fast = 0, 1
        while fast < len(nums) and nums[slow] + nums[fast] <= target:
            fast += 1

        fast = fast - 1
        while True:
            if slow >= fast:
                break
            if nums[slow] + nums[fast] == target:
                return [nums[slow], nums[fast]]
            elif nums[slow] + nums[fast] < target:
                slow += 1
            else:
                fast -= 1
        return []


"""
1. 双指针：使用快指针定位最大值，快慢指针同时向里移动 时间复杂度：O(n) 空间复杂度：O(1)
"""