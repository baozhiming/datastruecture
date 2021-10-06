from linkedList.removeNthFromEnd.remove_nth_from_end import Solution


def test_merge_two_list():
    solution = Solution()
    nums1 = [1, 2, 3, 7, 9, 3]
    l1 = solution.list2linked_list(nums1)
    l2 = solution.remove_nth_from_end(l1, 2)
    result = solution.echo_linked_list(l2)
    assert result == '1 -> 2 -> 3 -> 7 -> 3 -> None'
