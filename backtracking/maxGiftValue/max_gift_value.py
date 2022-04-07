# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直
# 到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
#
#
#
#  示例 1:
#
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
#
#
#
#  提示：
#
#
#  0 < grid.length <= 200
#  0 < grid[0].length <= 200
#
#  Related Topics 数组 动态规划 矩阵 👍 272 👎 0
from typing import List


class Solution:
    max_value = 0
    def getMaxGiftValue(self, nums: List[List[int]]) -> int:
        self.recurse(nums, 0, 0, nums[0][0])
        return self.max_value

    def recurse(self, nums: List[List[int]], i: int, j: int, cur_value: int):
        if i == len(nums) - 1 and j == len(nums[0]) - 1:
            if cur_value > self.max_value:
                self.max_value = cur_value
            return
        if i + 1 < len(nums):
            self.recurse(nums, i+1, j, cur_value + nums[i+1][j])
        if j + 1 < len(nums[0]):
            self.recurse(nums, i, j+1, cur_value + nums[i][j+1])


handler = Solution()
re = handler.getMaxGiftValue([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
])
print(re)
assert re == 12
