"""
归并排序
"""
from typing import List


class Solution:
    nums = 0
    def reversePairs(self, nums: List):
        if not nums or len(nums) == 1:
            return 1
        self.merge_sort(nums, 0, len(nums) - 1)
        return self.nums

    def merge_sort(self, nums: List, left: int, right: int):
        if left >= right:
            return
        middle = left + (right - left) // 2
        self.merge_sort(nums, left, middle)
        self.merge_sort(nums, middle + 1, right)
        self.merge(nums, left, middle, right)

    def merge(self, nums: List, left: int, middle: int, right: int):
        temp = []
        i, j = left, middle + 1
        while i <= middle and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                self.nums += (middle - i + 1)
                temp.append(nums[j])
                j += 1
        while i <= middle:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        nums[left:right+1] = temp


def merge_sort(nums: List) -> List:
    return recurse(nums, 0, len(nums) - 1)


def recurse(nums: List, left: int, right: int):
    if left >= right:
        return nums
    middle = left + int((right - left) / 2)
    recurse(nums, left, middle)
    recurse(nums, middle + 1, right)
    merge(nums, left, middle, right)
    return nums


def merge(nums: List, left: int, middle: int, right: int):
    pre, last = left, middle+1
    tmp_nums = []
    while pre <= middle and last <= right:
        if nums[pre] <= nums[last]:
            tmp_nums.append(nums[pre])
            pre += 1
        else:
            tmp_nums.append(nums[last])
            last += 1
    while pre <= middle:
        tmp_nums.append(nums[pre])
        pre += 1
    while last <= right:
        tmp_nums.append(nums[last])
        last += 1
    nums[left:right+1] = tmp_nums


"""
思想：分治思想，先将数组分为对等的两部分，对两部分进行排序。两部分排序完成后，将两个子数组合并
编程技巧：递归，递归公式：recurse(nums) = merge(recurse(nums[0, p]), recurse(p+1, r))
稳定的算法：是的。合并时将左边的数据优先选择
时间复杂度：根据递归公式，时间复杂度也可使用递归公式:
T(1) = K 
T(n) = 2T(n/2) + n
     = 4T(n/4) + 2n
     = 8T(n/8) + 3n
     = 16T(n/16) + 4n
     = 2^mT(n/2^m) + mn
n/2^m = 1 -> m = log(n)
所以：T(n) = nK + nlog(n)
所以时间复杂度为：nlog(n)。最好和最坏的时间复杂度一样
空间复杂度：O(n)。注意，空间复杂度不能像时间复杂度一样用递归公式计算，因为空间消耗不是累加的。
"""



handle = Solution()
a = handle.reversePairs([2, 4, 3, 1, 5, 6])
print(a)