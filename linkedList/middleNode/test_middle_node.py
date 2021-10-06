from linkedList.list_node import ListNode, list2linked_list, echo_linked_list
from linkedList.middleNode.middle_node import Solution


def test_middle_node():
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    head = list2linked_list(nums)
    middle_node = solution.middle_node(head)
    result = echo_linked_list(middle_node)
    assert result == '3 -> 4 -> 5 -> None'

    nums = [1, 2, 3, 4, 5, 6]
    head = list2linked_list(nums)
    middle_node = solution.middle_node(head)
    result = echo_linked_list(middle_node)
    assert result == '4 -> 5 -> 6 -> None'

    nums = []
    head = list2linked_list(nums)
    middle_node = solution.middle_node(head)
    result = echo_linked_list(middle_node)
    assert result == 'None'

    nums = [1]
    head = list2linked_list(nums)
    middle_node = solution.middle_node(head)
    result = echo_linked_list(middle_node)
    assert result == '1 -> None'

    nums = [1, 2]
    head = list2linked_list(nums)
    middle_node = solution.middle_node(head)
    result = echo_linked_list(middle_node)
    assert result == '2 -> None'
