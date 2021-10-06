from linkedList.reverseList.reverse_list import Solution


def test_reverse_list():
    solution = Solution()
    head = [1, 2, 3, 4, 5]
    head = solution.list2linked_list(head)
    result = solution.echo_linked_list(head)
    print(result)
    assert result == "1 -> 2 -> 3 -> 4 -> 5 -> None"
    head = solution.reverse_list(head)
    result = solution.echo_linked_list(head)
    assert result == "5 -> 4 -> 3 -> 2 -> 1 -> None"

    head = []
    head = solution.list2linked_list(head)
    assert head is None
    head = solution.reverse_list(head)
    assert head is None
    result = solution.echo_linked_list(head)
    assert result == "None"

    head = [1]
    head = solution.list2linked_list(head)
    result = solution.echo_linked_list(head)
    print(result)
    assert result == "1 -> None"
    head = solution.reverse_list(head)
    result = solution.echo_linked_list(head)
    assert result == "1 -> None"

    head = [1, 2]
    head = solution.list2linked_list(head)
    result = solution.echo_linked_list(head)
    print(result)
    assert result == "1 -> 2 -> None"
    head = solution.reverse_list(head)
    result = solution.echo_linked_list(head)
    assert result == "2 -> 1 -> None"
