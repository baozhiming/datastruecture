"""
编辑距离，使用莱文斯坦方法实现，只允许添加、删除、替换三个操作
"""
import sys


class Solution:
    def edit_distance(self, a: str, b: str) -> int:
        """回溯算法"""
        min_edit = sys.maxsize

        def backtracking(i: int, j: int, edit: int):
            nonlocal min_edit, a, b
            if i == len(a) and j == len(b):
                if edit < min_edit:
                    min_edit = edit
                return
            elif i == len(a) or j == len(b):
                temp = edit + len(b) - j if j < len(b) else edit + len(a) - i
                if temp < min_edit:
                    min_edit = temp
                return

            if a[i] == b[j]:
                backtracking(i+1, j+1, edit)
            else:
                backtracking(i+1, j, edit+1)
                backtracking(i, j+1, edit+1)
                backtracking(i+1, j+1, edit+1)

        backtracking(0, 0, 0)
        if min_edit == sys.maxsize:
            return 0
        return min_edit

    def edit_distance_by_dp(self, a: str, b: str) -> int:
        if not a or not b:
            if a:
                return len(a)
            elif b:
                return len(b)
            else:
                return 0
        states = [[0 for i in range(len(b))] for _ in range(len(a))]
        states[0][0] = 0 if a[0] == b[0] else 1
        for i in range(1, len(a)):
            states[i][0] = states[i-1][0] + 1
        for i in range(1, len(b)):
            states[0][i] = states[0][i] + 1

        for i in range(1, len(a)):
            for j in range(1, len(b)):
                if a[i] == b[j]:
                    states[i][j] = min(states[i - 1][j - 1], states[i - 1][j] + 1, states[i][j - 1] + 1)
                else:
                    states[i][j] = min(states[i - 1][j - 1] + 1, states[i - 1][j] + 1, states[i][j - 1] + 1)

        return states[len(a) - 1][len(b) - 1]


handler = Solution()
re = handler.edit_distance("mitcmu", "mtacnu")
print(re)
assert re == 3

re = handler.edit_distance("mitcmu", "mtacnudd")
print(re)
assert re == 5

re = handler.edit_distance_by_dp("mitcmu", "mtacnu")
print(re)
assert re == 3

re = handler.edit_distance_by_dp("mitcmu", "mtacnudd")
print(re)
assert re == 5

re = handler.edit_distance_by_dp("", "mitcmu")
print(re)
assert re == 6

re = handler.edit_distance_by_dp("mitcmu", "")
print(re)
assert re == 6
