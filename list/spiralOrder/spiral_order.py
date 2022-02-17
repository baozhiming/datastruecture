"""
顺时针螺旋打印二维数组
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        re = []
        if not matrix:
            return re

        def recurse(matrix: List[List[int]], l_begin, l_end, c_begin, c_end):
            if l_begin > l_end or c_begin > c_end:
                return
            i, j = l_begin, c_begin
            while True:
                if i == l_begin + 1 and j == c_begin != c_end:
                    re.append(matrix[i][j])
                    break
                re.append(matrix[i][j])
                if l_begin == l_end and j == c_end:
                    break
                elif i == l_end and c_begin == c_end:
                    break
                elif i == l_begin and j < c_end:
                    j += 1
                elif i < l_end and j == c_end:
                    i += 1
                elif i == l_end and j > c_begin:
                    j -= 1
                elif i > l_begin and j == c_begin:
                    i -= 1
                else:
                    break
            recurse(matrix, i, l_end-1, j+1, c_end-1)

        recurse(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
        return re

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        """
                1. 初始化矩阵，用来存储每个元素是否被访问过。初始化方向。
                """
        if not matrix:
            return matrix
        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direc_index = 0
        row, column = 0, 0
        re = []
        for i in range(total):
            re.append(matrix[row][column])
            visited[row][column] = True

            # 模拟下一步
            next_row, next_column = row + directions[direc_index][0], column + directions[direc_index][1]
            if not (0 <= next_row < rows and 0 <= next_column < columns and visited[next_row][next_column] != True):
                direc_index = (direc_index + 1) % 4
            row, column = row + directions[direc_index][0], column + directions[direc_index][1]
        return re


if __name__ == "__main__":
    array = [[2, 5], [8, 4], [0, -1]]
    handler = Solution()
    print(handler.spiralOrder(array))