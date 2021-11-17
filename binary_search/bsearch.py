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


def search_left_element(nums: List, n: int) -> int:
    """查找第一个值等于给定值的元素"""
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] == n:
            re = middle - 1
            while re >= 0 and nums[re] == n:
                re -= 1
            return re + 1
        elif nums[middle] > n:
            high = middle - 1
        else:
            low = middle + 1
    return -1


def search_right_element(nums: List, n: int) -> int:
    """查找最后一个值等于给定值的元素"""
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] == n:
            re = middle + 1
            while re < len(nums) and nums[re] == n:
                re += 1
            return re - 1
        elif nums[middle] > n:
            high = middle - 1
        else:
            low = middle + 1
    return -1


def bsearch_left_not_less(nums: List, n: int) -> int:
    """查找第一个大于等于给定值的元素"""
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] >= n:
            re = middle - 1
            while re >= 0 and nums[re] >= n:
                re -= 1
            return re + 1
        else:
            low = middle + 1
    return -1


def bsearch_right_not_greater(nums: List, n: int) -> int:
    """查找最后一个小于等于给定值的元素"""
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] <= n:
            re = middle + 1
            while re < len(nums) and nums[re] <= n:
                re += 1
            return re - 1
        else:
            high = middle - 1
    return -1



"""
上面四个变形找到中间值后，使用顺序遍历的方式找到目标值，复杂度升高。
"""


def search_left_element_2(nums: List, n: int) -> int:
    """查找第一个值等于给定值的元素"""
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] > n:
            high = middle - 1
        elif nums[middle] < n:
            low = middle + 1
        else:
            if middle == 0 or nums[middle - 1] != n:
                return middle
            else:
                high = middle -1
    return -1


def search_right_element_2(nums: List, n: int) -> int:
    """查找最后一个值等于给定值的元素"""
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] > n:
            high = middle - 1
        elif nums[middle] < n:
            low = middle + 1
        else:
            if middle == len(nums) - 1 or nums[middle + 1] != n:
                return middle
            else:
                low = middle + 1
    return -1


def bsearch_left_not_less_2(nums: List, n: int) -> int:
    """查找第一个大于等于给定值的元素"""
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] >= n:
            if middle == 0 or nums[middle - 1] < n:
                return middle
            else:
                high = middle - 1
        else:
            low = middle + 1
    return -1


def bsearch_right_not_greater2(nums: List, n: int) -> int:
    """查找最后一个小于等于给定值的元素"""
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] <= n:
            if middle == len(nums) - 1 or nums[middle + 1] > n:
                return middle
            else:
                low = middle + 1
        else:
            high = middle - 1
    return -1


def bsearch_in_cycle_order_array(nums: List, n: int) -> int:
    """返回循环有序数组中，值等于给定值的元素, 没有重复的元素
    方法：先找分界点，判断区间，再找给定值
    TODO 时间复杂度是2O(log(n))还是O(n)
    """
    low = 0
    high = len(nums) - 1
    divide = 0
    # 1. 找到分界点：最后一个大于等于第一个元素的值
    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] < nums[0]:
            high = middle - 1
        elif nums[middle] >= nums[0]:
            if middle == len(nums) - 1 or nums[middle + 1] < nums[0]:
                divide = middle
                break
            else:
                low = middle + 1
        # else:
            # TODO 第一次此处出错了， middle处于0时，也可能不是最后一个元素
            # divide = middle
            # break

    if nums[0] <= n <= nums[divide]:
        low = 0
        high = divide
    else:
        low = divide + 1 if divide < len(nums) - 1 else divide
        high = len(nums) - 1

    while low <= high:
        middle = low + (high - low) // 2
        if nums[middle] == n:
            return middle
        elif nums[middle] > n:
            high = middle - 1
        else:
            low = low + 1
    return -1
