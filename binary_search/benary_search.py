from typing import List


def binary_search(nums: List, n: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] > n:
            high = middle - 1
        elif nums[middle] < n:
            low = middle + 1
        else:
            return middle
    return -1


def binary_search_recurse(nums: List, n: int) -> int:
    return recurse(nums, 0, len(nums) - 1, n)


def recurse(nums: List, low: int, high: int, n: int) -> int:
    if low > high:
        return -1
    middle = low + (high - low) // 2
    if nums[middle] > n:
        return recurse(nums, low, middle - 1, n)
    elif nums[middle] < n:
        return recurse(nums, middle + 1, high, n)
    else:
        return middle
