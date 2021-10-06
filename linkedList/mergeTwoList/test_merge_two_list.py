from linkedList.mergeTwoList.merge_two_list import Solution


def test_merge_two_list():
    solution = Solution()
    nums1 = [1, 2, 3]
    nums2 = [1, 3, 4]
    l1 = solution.list2linked_list(nums1)
    result = solution.echo_linked_list(l1)
    assert result == '1 -> 2 -> 3 -> None'
    l2 = solution.list2linked_list(nums2)
    result = solution.echo_linked_list(l2)
    assert result == '1 -> 3 -> 4 -> None'
    head = solution.mergeTwoLists(l1, l2)
    result = solution.echo_linked_list(head)
    assert result == '1 -> 1 -> 2 -> 3 -> 3 -> 4 -> None'

    nums1 = [1, 2, 3]
    nums2 = [1, 3, 4]
    l1 = solution.list2linked_list(nums1)
    result = solution.echo_linked_list(l1)
    assert result == '1 -> 2 -> 3 -> None'
    l2 = solution.list2linked_list(nums2)
    result = solution.echo_linked_list(l2)
    assert result == '1 -> 3 -> 4 -> None'
    head = solution.merge_two_lists_by_recurse(l1, l2)
    result = solution.echo_linked_list(head)
    assert result == '1 -> 1 -> 2 -> 3 -> 3 -> 4 -> None'
