from stack.backSpaceCompare.back_space_compare import Solution


def test_():
    solution = Solution()
    s = "ab#c"
    b = "ad#c"
    re = solution.back_space_compare(s, b)
    assert re is True

    s = "ab##"
    t = "c#d#"
    re = solution.back_space_compare(s, t)
    assert re is True

    s = "a##b"
    t = '#c#b'
    re = solution.back_space_compare(s, t)
    assert re is True

    s = "a##c"
    t = '#c#b'
    re = solution.back_space_compare(s, t)
    assert re is False

    s = "ab#c"
    b = "ad#c"
    re = solution.back_space_compare_by_one_space_true(s, b)
    assert re is True

    s = "ab##"
    t = "c#d#"
    re = solution.back_space_compare_by_one_space_true(s, t)
    assert re is True

    s = "a##b"
    t = '#c#b'
    re = solution.back_space_compare_by_one_space_true(s, t)
    assert re is True

    s = "a##c"
    t = '#c#b'
    re = solution.back_space_compare_by_one_space_true(s, t)
    assert re is False
