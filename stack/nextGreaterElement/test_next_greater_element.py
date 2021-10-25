from stack.nextGreaterElement.next_greater_element import Solution


def test_next_greater():
    solution = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    re = solution.nextGreaterElement(nums1, nums2)
    assert re == [-1, 3, -1]

    nums1 = [2,4]
    nums2 = [1,2,3,4]
    re = solution.nextGreaterElement(nums1, nums2)
    assert re == [3, -1]