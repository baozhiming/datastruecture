# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。
#  示例：
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。
#  提示：
#  0 <= nums.length <= 50000
#  0 <= nums[i] <= 10000
#
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1:
            return []
        first_even = None
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if first_even is None:
                    first_even = i
            else:
                if first_even is not None:
                    tmp = nums[first_even]
                    nums[first_even] = nums[i]
                    nums[i] = tmp
                    first_even += 1
        return nums

