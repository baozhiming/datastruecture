#  给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#
#  
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#  
#
# 提示：
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 10
#
# 代码：
from typing import List


class Solution:
    max_sub_length = 0

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.recurse(nums, 0, -200, 0)
        return self.max_sub_length

    def recurse(self, nums: List[int], index: int, cur_tmp: int, cur_count):
        if index == len(nums):
            if cur_count > self.max_sub_length:
                self.max_sub_length = cur_count
            return
        self.recurse(nums, index + 1, cur_tmp, cur_count)
        if nums[index] > cur_tmp:
            self.recurse(nums, index + 1, nums[index], cur_count + 1)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        states = [[None for _ in range(len(nums))] for _ in range(len(nums))]
        states[0][0] = 1
        for i in range(1, len(nums)):
            states[i][i] = 1
            # 不选
            for j in range(i):
                states[i][j] = states[i-1][j]
            # 选
            for j in range(i):
                if nums[j] < nums[i] and states[i][j] + 1 > states[i][i]:
                    states[i][i] = states[i][j] + 1
        count = 1
        for i in states[-1]:
            if i > count:
                count = i
        return count


handler = Solution()
re = handler.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print(re)
assert re == 4

handler = Solution()
re = handler.lengthOfLIS([0, 1, 0, 3, 2, 3])
print(re)
assert re == 4

handler = Solution()
re = handler.lengthOfLIS([7, 7, 7, 7, 7, 7, 7])
print(re)
assert re == 1

handler = Solution()
re = handler.lengthOfLIS([])
print(re)
assert re == 0


handler = Solution()
re = handler.lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18])
print(re)
assert re == 4

handler = Solution()
re = handler.lengthOfLIS2([0, 1, 0, 3, 2, 3])
print(re)
assert re == 4

handler = Solution()
re = handler.lengthOfLIS2([7, 7, 7, 7, 7, 7, 7])
print(re)
assert re == 1

handler = Solution()
re = handler.lengthOfLIS2([])
print(re)
assert re == 0

handler = Solution()
re = handler.lengthOfLIS2([4,10,4,3,8,9])
print(re)
assert re == 3