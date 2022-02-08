"""
给定排序数组，和一个元素，返回元素在数组中出现的次数
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        first = None
        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] == target:
                if middle == 0 or nums[middle - 1] < target:
                    first = middle
                    break
                else:
                    high = middle - 1
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1

        if first is None:
            return 0

        low, high = first, len(nums) - 1
        last = None
        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] > target:
                if middle > 0 and nums[middle - 1] <= target:
                    last = middle
                    break
                else:
                    high = middle - 1
            else:
                low = middle + 1

        if last is None:
            last = len(nums)

        return last - first


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    handler = Solution()
    assert handler.search(nums, target) == 2

    target = 6

    assert handler.search(nums, target) == 0

    nums = [1]
    target = 1
    print(handler.search(nums, target))
