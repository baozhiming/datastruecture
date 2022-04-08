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
#  Related Topics 数组 动态规划 矩阵 👍 276 👎 0
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """使用回溯算法
        时间复杂度：2^(m + n)
        空间：1
        """
        max_value = 0

        def backtracking(matrix: List[List[int]], row: int, col: int, cur_value: int):
            nonlocal max_value
            if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
                if cur_value > max_value:
                    max_value = cur_value
                return
            if row + 1 < len(matrix):
                backtracking(matrix, row + 1, col, cur_value + matrix[row+1][col])
            if col + 1 < len(matrix[0]):
                backtracking(matrix, row, col + 1, cur_value + matrix[row][col+1])

        if not grid:
            return max_value
        backtracking(grid, 0, 0, grid[0][0])
        return max_value

    def maxValueByDP(self, grid: List[List[int]]) -> int:
        """
        动态规划
        时间复杂度：m * n
        空间复杂度：m * n
        :param grid:
        :return:
        """
        if not grid:
            return 0
        states = [[0 for i in range(len(grid[0]))] for _ in range(len(grid))]
        states[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            states[i][0] = states[i-1][0] + grid[i][0]
        for i in range(1, len(grid[0])):
            states[0][i] = states[0][i-1] + grid[0][i]

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                cur_max_value = max(states[row-1][col], states[row][col-1])
                states[row][col] = cur_max_value + grid[row][col]
        return states[-1][-1]


handler = Solution()
re = handler.maxValue([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
print(re)
assert re == 12


re = handler.maxValue([])
print(re)
assert re == 0

re = handler.maxValue([[1, 3, 1]])
print(re)
assert re == 5

re = handler.maxValue([[1], [1], [4]])
print(re)
assert re == 6


re = handler.maxValueByDP([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
print(re)
assert re == 12


re = handler.maxValueByDP([])
print(re)
assert re == 0

re = handler.maxValueByDP([[1, 3, 1]])
print(re)
assert re == 5

re = handler.maxValueByDP([[1], [1], [4]])
print(re)
assert re == 6