from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        循环数组中，最小的值。数组中不存在重复的值
        注意：为什么要和最高位的值做比较？和最低位的值做比较行不行？ 这个问题可以通过升序数组来做判断。如果和地位元素比较会有问题。
        判断条件为什么是 < 不是<=。在数组中寻找某个值时，需要判断没有一个值。所以包含==，而获取最小值时，当low==high时，就定位到了最小值，不用在判断
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            middle = low + (high - low) // 2
            if nums[middle] >= nums[high]:
                low = middle + 1
            else:
                high = middle
        return nums[low]

    def minArray2(self, nums: List[int]) -> int:
        """
        循环数组中，最小的值。数组中可能存在重复的值
        因为有重复的数组，所有在中间元素等于最高元素时，不能确定要省略左半部分还是右半部分。
        但是因为middle元素等于high元素，所以无论high元素是最小值还是不是最小值，这个high都不重要了，因为有middle值替代。所以high直接取前一位。
        """
        low, high = 0, len(nums) - 1
        while low < high:
            middle = low + (high - low) // 2
            if nums[middle] == nums[high]:
                high = high - 1
            elif nums[middle] > nums[high]:
                low = middle + 1
            else:
                high = low
        return nums[low]


if __name__ == "__main__":
    handler = Solution()
    nums = [4, 5, 6, 7, 8, 9, 2, 3]
    print(handler.findMin(nums))

    nums = [1, 2, 3, 4, 5]
    print(handler.findMin(nums))

    nums = [2, 1]
    print(handler.findMin(nums))