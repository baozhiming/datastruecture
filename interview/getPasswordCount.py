# 求手机手势密码数量
# o o o
# o o o
# o o o
# 1) 要求手势密码长度至少为3 （至少经过3个点）且连续
# 2) 同一个密码不能有环（不能经过同一个点两次）
# 3) 连线方向(1,0) (0, 1) (-1,0) (0,-1) (1,1) (1,-1) (-1,1) (-1,-1)
from typing import List


class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0

    def get_password_count(self) -> int:
        """回溯算法的思想
        实现语言：python3
        """
        for i in range(3):
            for j in range(3):
                states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                self.dfs(i, j, 1, states)
        return Solution.count

    def dfs(self, i: int, j: int, curr_len: int, states: List[List]):
        if states[i][j] == 1:
            return
        if curr_len >= 3:
            Solution.count += 1
            states[i][j] = 1
            print(states[0])
            print(states[1])
            print(states[2])
            print("=====")
            states[i][j] = 0
        for direction in Solution.directions:
            if 0 <= i + direction[0] < 3 and 0 <= j + direction[1] < 3 and states[i + direction[0]][j + direction[1]] != 1:
                states[i][j] = 1
                self.dfs(i + direction[0], j + direction[1], curr_len + 1, states)
                states[i][j] = 0


handler = Solution()
re = handler.get_password_count()
print(re)

