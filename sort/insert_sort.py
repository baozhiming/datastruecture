"""
插入排序
插入排序将数组分为已排序区间和未排序区间两个部分。
每次从未排序区间选择一个元素，插入到已排序区间（找到插入位置，搬移数据，插入）
"""
from typing import List


def insert_sort(nums: List) -> List:
    if not nums or len(nums) == 1:
        return nums
    for i in range(1, len(nums)):
        j = i - 1
        value = nums[i]
        # 这个地方要注意，当j为-1时，如果value小，则会将最后一个元素赋值给0，但是21行会覆盖掉。
        for j in range(i-1, -2, -1):
            if value < nums[j]:
                nums[j+1] = nums[j]
            else:
                break
        nums[j+1] = value
    return nums



"""
原地？是的
稳定：是的
时间复杂度：
最好：n 满有序度
最坏：n^2，逆有序度等于满有序度
平均：O(n^2),每次将数据插入到数组的平均复杂度为n，循环n次。n2
"""