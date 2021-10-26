"""
归并排序
"""
from typing import List


def merge_sort(nums: List) -> List:
    if not nums or len(nums) == 1:
        return nums
    return recurse(nums, 0, len(nums) - 1)


def recurse(nums: List, l: int, r: int):
    if l >= r:
        return nums
    q = int((l + r) / 2)
    nums1 = recurse(nums, l, q)
    nums2 = recurse(nums, q+1, r)
    re = merge(nums1, l, q, nums2, q+1, r)
    return re


def merge(nums1: List, l1, r1, nums2: List, l2, r2) -> List:
    i, j, k = l1, l2, 0
    nums = []
    while i <= r1 and j <= r2:
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    while i <= r1:
        nums.append(nums1[i])
        i += 1
    while j <= r2:
        nums.append(nums2[j])
        j += 1
    nums1[l1:r2+1] = nums
    return nums1


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
