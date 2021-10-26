"""
快速排序
"""
from typing import List


def quick_sort(nums: List) -> List:
    if not nums or len(nums) == 1:
        return nums
    return recurse(nums, 0, len(nums) - 1)


def recurse(nums: List, l: int, r: int) -> List:
    if l >= r:
        return nums
    q = partition(nums, l, r)
    recurse(nums, l, q - 1)
    recurse(nums, q + 1, r)
    return nums


def partition(nums, l, r) -> int:
    pilvot = r
    i = l
    for j in range(l, r):
        if nums[j] < nums[pilvot]:
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp
            i += 1
    tmp = nums[pilvot]
    nums[pilvot] = nums[i]
    nums[i] = tmp
    return i


"""
思想：分治思想，先对数组进行分区，将小于分区点和大于分区点的数据分开。对左右两部分分别进行排序
是稳定的算法吗？不是，因为分区之后直接交换元素。
是原地的算法吗？是的，因为分区操作不需要额外的存储
时间复杂度：
当分区点非常的均匀，每次分区点分区后都在数组的中间位置：
T(n) = n + 2T(n/2)
     = 4T(n/4) + 2n
     = 2^m T(n/2^m) + mn
T(n) = nlog(n)

分区点都分布在边上，此时时间复杂度为n^2
平均时间复杂度？
"""
