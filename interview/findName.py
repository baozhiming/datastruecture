# 给你一个姓名数组names，数组里有重复姓名，请你剔除重复姓名，返回不包含重复姓名的数组长度。
# 备注：如果给你任意一个名字，怎么知道重复了多少次。
#
# 示例 1：
#
# 输入：names= ["Tom","Jerry","Athur","Tom","Gerard","Cori","Cori"]
# 输出：5
# 这道题就是考察了能不能对应不同的场景使用不同的数据结构，也就是能不能想到使用散列表。

from typing import List


class Solution:
    def find_name(self, nums: List) -> int:
        hashmap = dict()
        count = 0
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
                count += 1
            hashmap[i] += 1
        return count


handler = Solution()
re = handler.find_name(["Tom","Jerry","Athur","Tom","Gerard","Cori","Cori"])
print(re)
