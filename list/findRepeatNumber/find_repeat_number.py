
from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:
                continue
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                tmp = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp
        return -1



"""
暴力解法：双层迭代，时间复杂度为n^2
利用空间换时间的思想：利用散列表，存储出现过的字符，如果重复出现，则返回。时间复杂度为n，空间复杂度为n
原地算法：因为题目中有一个限制条件：数组中的数字都是小于n的。所以便有了将元素放到元素值对应的下标位置上。如果已经找到过了，则发现重复。
"""