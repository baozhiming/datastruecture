# 给定一个数组prices ，它的第i个元素prices[i]表示一支给定股票第i天的价格。你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回何利润，返回
# 0 。
#
#
#
# 示例
# 1：
#
# 输入：[7, 1, 5, 3, 6, 4]
# 输出：5
# 解释：在第
# 2
# 天（股票价格 = 1）的时候买入，在第
# 5
# 天（股票价格 = 6）的时候卖出，最大利润 = 6 - 1 = 5 。
# 注意利润不能是
# 7 - 1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#
# 示例
# 2：
#
# 输入：prices = [7, 6, 4, 3, 1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为
# 0。
#
#
#
# 提示：
#
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
import sys
from typing import List


class Solution:
    def max_profit(self, prices: List):
        max_profit = 0
        has_profit = False
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[j-1]:
                    has_profit = True
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
            if not has_profit:
                break
        return max_profit

    def max_profit2(self, prices: List):
        min_value = prices[0]
        max_profit = 0
        if not prices:
            return max_profit
        for i in range(1, len(prices)):
            if prices[i] > min_value:
                max_profit = max(max_profit, prices[i] - min_value)
            if prices[i] < min_value:
                min_value = prices[i]
        return max_profit


handler = Solution()
re = handler.max_profit([7, 1, 5, 3, 6, 4])
print(re)
assert re == 5
re = handler.max_profit([7, 6, 4, 3, 1])
print(re)
assert re == 0


handler = Solution()
re = handler.max_profit2([7, 1, 5, 3, 6, 4])
print(re)
assert re == 5
re = handler.max_profit2([7, 6, 4, 3, 1])
print(re)
assert re == 0

"""
方法1：第一次实现双层遍历时，没有考虑优化空间
优化特殊情况：单调递减数组，遍历一次便可提前推出
这个方法的时间复杂度是n^2，肯定是不满足要求的
方案2：选择最低点，假设买入都在最低点，然后每次卖出与买入点对比。一次遍历
这道题和求最长递增子数组的题是都是华为面试官出的题。这道题我刚做的时候说了一句，两道题是相似的。当面试官总结的时候，说了这两道题是完全不一样的解决思路的题。
因为我都没有做出来，所以考察到我对于不同的题，不能够作出正确的解题方法结论。
这个题，当时我连暴力解法都没有去想，一直在想王争教的动态规划，往上面死套，把自己套进去了
这也是动态规划的一种没见过的题型

"""