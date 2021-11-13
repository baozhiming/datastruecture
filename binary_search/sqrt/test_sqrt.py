from binary_search.sqrt.sqrt import Solution


def test_sqrt():
    solution = Solution()
    assert solution.sqrt(9) == 3

    assert solution.sqrt(0) == 0

    assert solution.sqrt(16) == 4

    assert solution.sqrt(1) == 1

    assert solution.sqrt(5) == 1