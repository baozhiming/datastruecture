from linkedList.list_node import list2linked_list, echo_linked_list
from linkedList.palindroom.is_palindrome import Solution


def test_is_palindrome():
    solution = Solution()
    nums = [1, 2, 2, 1]
    head = list2linked_list(nums)
    result = echo_linked_list(head)
    assert result == '1 -> 2 -> 2 -> 1 -> None'
    is_palindrome = solution.is_palindrome(head)
    assert is_palindrome is True

    nums = [1, 2, 5, 2, 1]
    head = list2linked_list(nums)
    result = echo_linked_list(head)
    assert result == '1 -> 2 -> 5 -> 2 -> 1 -> None'
    is_palindrome = solution.is_palindrome(head)
    assert is_palindrome is True

    nums = [1, 2]
    head = list2linked_list(nums)
    result = echo_linked_list(head)
    assert result == '1 -> 2 -> None'
    is_palindrome = solution.is_palindrome(head)
    assert is_palindrome is False

    nums = [1]
    head = list2linked_list(nums)
    result = echo_linked_list(head)
    assert result == '1 -> None'
    is_palindrome = solution.is_palindrome(head)
    assert is_palindrome is True

    nums = []
    head = list2linked_list(nums)
    result = echo_linked_list(head)
    assert result == 'None'
    is_palindrome = solution.is_palindrome(head)
    assert is_palindrome is True

