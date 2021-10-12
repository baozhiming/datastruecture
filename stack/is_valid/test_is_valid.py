from stack.is_valid.is_valid import Solution


def test_is_valid():
    solution = Solution()
    s = '()'
    re = solution.isValid(s)
    assert re is True

    s = "()[]{}"
    re = solution.isValid(s)
    assert re is True

    s = "(]"
    re = solution.isValid(s)
    assert re is False
