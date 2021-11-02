from sort.reversePairs.reverse_pairs import Solution


def test_reverse_pairs():
    solution = Solution()
    nums = [7, 5, 6, 4]
    re = solution.reverse_pairs(nums)
    assert re == 5
