"""
编辑距离，使用最长公共子串长度计算，仅支持删除和增加两个操作
"""
from typing import List


class Solution:
    def edit_distance(self, a: str, b: str) -> int:
        """
        回溯算法
        :param a:
        :param b:
        :return:
        """
        max_common_sub = 0

        def backtracking(i: int, j: int, common_sub: int):
            nonlocal a, b, max_common_sub
            if i == len(a) or j == len(b):
                if common_sub > max_common_sub:
                    max_common_sub = common_sub
                return
            if a[i] == b[j]:
                backtracking(i+1, j+1, common_sub+1)
            else:
                backtracking(i, j+1, common_sub)
                backtracking(i+1, j, common_sub)
        backtracking(0, 0, 0)
        return max_common_sub

    def edit_distance_by_dp(self, a: str, b: str) -> int:
        """
        使用动态规划
        :param a:
        :param b:
        :return:
        """
        if not a or not b:
            return 0
        states = [[0 for i in range(len(b))] for _ in range(len(a))]
        states[0][0] = 1 if a[0] == b[0] else 0
        for i in range(1, len(a)):
            states[i][0] = states[i-1][0]
        for i in range(1, len(b)):
            states[0][i] = states[0][i-1]

        for i in range(1, len(a)):
            for j in range(1, len(b)):
                if a[i] == b[j]:
                    states[i][j] = max(states[i - 1][j - 1] + 1, states[i - 1][j], states[i][j - 1])
                else:
                    states[i][j] = max(states[i - 1][j - 1], states[i - 1][j], states[i][j - 1])
        return states[-1][-1]


handler = Solution()
re = handler.edit_distance("mitcmu", "mtacnu")
print(re)
assert re == 4


re = handler.edit_distance_by_dp("mitcmu", "mtacnu")
print(re)
assert re == 4
