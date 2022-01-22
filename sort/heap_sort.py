"""
堆排序
"""
from typing import List


def heap_sort(nums: List) -> List:
    if not nums or len(nums) == 1:
        return nums

    # 1. 建堆
    for i in range(len(nums) // 2 - 1, -1, -1):
        heapify(nums, len(nums) - 1, i)

    # 2. 排序
    for i in range(len(nums) - 1, -1, -1):
        swap(nums, 0, i)
        heapify(nums, i - 1, 0)
    return nums


def heapify(nums: List, end: int, i: int):
    while True:
        if i * 2 + 2 <= end:
            max_point = i * 2 + 2 if nums[i * 2 + 2] > nums[i * 2 + 1] else i * 2 + 1
        elif i * 2 + 1 <= end:
            max_point = i * 2 + 1
        else:
            max_point = None

        if max_point is None or nums[i] >= nums[max_point]:
            break

        swap(nums, i, max_point)
        i = max_point


def swap(nums: List, i: int, j: int):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


if __name__ == "__main__":
    array = [7, 5, 19, 8, 4, 1, 20, 13, 16, 15]
    re = heap_sort(array)
    print(re)


"""
1。 建堆
使用了完全二叉树的特性：从零开始存储堆，n / 2 到n - 1 为叶子节点
2。 排序
"""
