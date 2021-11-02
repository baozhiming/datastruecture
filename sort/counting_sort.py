"""计数排序"""


from typing import List


def counting_sort(nums: List) -> List:
    if len(nums) == 0 or len(nums) == 1:
        return nums
    # 1. 获取数据范围
    max_ = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_:
            max_ = nums[i]

    # 2. 生成计数数组
    counts = [0] * (max_ + 1)
    for i in range(0, len(nums)):
        counts[nums[i]] += 1

    # 累加
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    # 3. 计数
    re = [0] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        re[counts[nums[i]] - 1] = nums[i]
        counts[nums[i]] -= 1

    # 4. 覆盖原数组
    nums = re
    return nums


a = [2, 5, 3, 0, 2, 3, 0, 3]
re = counting_sort(a)
print(re)
assert re == [0, 0, 2, 2, 3, 3, 3, 5]