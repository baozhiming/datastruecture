import pytest
from list.findKthLargest.find_kth_largest import Solution


def test_find_kth_largest():
    handler = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = handler.findKthLargest(nums, k)
    assert result == 5

    k = 4
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    result = handler.findKthLargest(nums, k)
    assert result == 4
