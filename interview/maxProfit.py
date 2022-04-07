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
from typing import List


class Solution:
    def max_profit(self, nums: List):
        max_profit = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] - nums[i] > max_profit:
                    max_profit = nums[j] - nums[i]
        return max_profit


handler = Solution()
re = handler.max_profit([7, 1, 5, 3, 6, 4])
print(re)
assert re == 5
re = handler.max_profit([7, 6, 4, 3, 1])
print(re)
assert re == 0