# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。
#
#  你可以认为每种硬币的数量是无限的。
#
#
#
#  示例 1：
#
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
#  示例 2：
#
#
# 输入：coins = [2], amount = 3
# 输出：-1
#
#  示例 3：
#
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
#  示例 4：
#
#
# 输入：coins = [1], amount = 1
# 输出：1
#
#
#  示例 5：
#
#
# 输入：coins = [1], amount = 2
# 输出：2
#
#
#
#
#  提示：
#
#
#  1 <= coins.length <= 12
#  1 <= coins[i] <= 2³¹ - 1
#  0 <= amount <= 10⁴
#
#
#
#
#  注意：本题与主站 322 题相同： https://leetcode-cn.com/problems/coin-change/
#  Related Topics 广度优先搜索 数组 动态规划 👍 32 👎 0
import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        states = [[None for i in range(amount+1)] for _ in range(len(coins))]
        count = 0
        while count * coins[0] <= amount:
            states[0][count * coins[0]] = count
            count += 1

        for row in range(1, len(coins)):
            for col in range(amount+1):
                if states[row-1][col] is None:
                    continue
                count = 0
                while True:
                    temp = col + count * coins[row]
                    if temp > amount:
                        break
                    if states[row-1][temp] is None:
                        states[row][temp] = states[row-1][col]+count
                    else:
                        if states[row][temp] is None:
                            states[row][temp] = min(states[row-1][temp], states[row-1][col]+count)
                        else:
                            states[row][temp] = min(states[row][temp], states[row - 1][col] + count)
                    count += 1

        min_count = states[0][-1]
        print(states[0][-1])
        for i in range(1, len(coins)):
            print(states[i][-1])
            if min_count is None:
                min_count = states[i][-1]
                continue
            if states[i][-1] is not None and states[i][-1] < min_count:
                min_count = states[i][-1]
        if min_count is None:
            min_count = -1
        return min_count

#
handler = Solution()
# re = handler.coinChange([3, 5, 1], 9)
# print(re)
# assert re == 3
#
#
# re = handler.coinChange([1, 3, 5], 9)
# print(re)
# assert re == 3
#
#
# re = handler.coinChange([1, 2, 5], 11)
# print(re)
# assert re == 3
#
#
# re = handler.coinChange([2], 3)
# print(re)
# assert re == -1
#
#
# re = handler.coinChange([1], 0)
# print(re)
# assert re == 0
#
#
# re = handler.coinChange([1], 1)
# print(re)
# assert re == 1
#
#
# re = handler.coinChange([1], 2)
# print(re)
# assert re == 2

re = handler.coinChange([478, 487, 16, 338], 1990)
print(re)
assert re == 15

