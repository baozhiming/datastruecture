from stack.calculate.calculate import Solution


def test_calculate():
    handler = Solution()
    s = "1 + 1"
    assert handler.calculate1(s) == 2

    s = "2-1 + 2 "
    assert handler.calculate1(s) == 3

    s = "(1+(4+5+2)-3)+(6+8)"
    assert handler.calculate1(s) == 23

    s = "2147483647"
    assert handler.calculate1(s) == 2147483647

    s = "   (  3 ) "
    assert handler.calculate1(s) == 3

    s = "-2+ 1"
    assert handler.calculate1(s) == -1
