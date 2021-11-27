from binary_search.bsearch import (search_left_element_2, search_right_element_2,
                                   bsearch_left_not_less_2, bsearch_right_not_greater2,
                                   bsearch_in_cycle_order_array, bsearch_in_cycle_order_array_by_recurse,
                                   bsearch_in_cycle_order_array_2)


def test_search_left_element_2():
    nums = [1, 2, 3, 3, 3, 5, 6]
    assert search_left_element_2(nums, 3) == 2

    nums = [1]
    assert search_left_element_2(nums, 3) == -1

    nums = [1]
    assert search_left_element_2(nums, 1) == 0

    nums = [1, 3, 3, 3, 3, 5, 6]
    assert search_left_element_2(nums, 3) == 1

    nums = []
    assert search_left_element_2(nums, 3) == -1

    nums = [1, 1, 3, 3, 3, 5, 6]
    assert search_left_element_2(nums, 1) == 0


def test_search_right_element_2():
    nums = [1, 2, 3, 3, 3, 5, 6]
    assert search_right_element_2(nums, 3) == 4

    nums = [1]
    assert search_right_element_2(nums, 3) == -1

    nums = [1]
    assert search_right_element_2(nums, 1) == 0

    nums = [1, 3, 3, 3, 3, 3, 3]
    assert search_right_element_2(nums, 3) == 6

    nums = []
    assert search_right_element_2(nums, 3) == -1

    nums = [1, 1, 3, 3, 3, 5, 6]
    assert search_right_element_2(nums, 1) == 1


def test_bsearch_left_not_less_2():
    nums = [1, 2, 3, 3, 3, 5, 6]
    assert bsearch_left_not_less_2(nums, 3) == 2

    nums = [1]
    assert bsearch_left_not_less_2(nums, 3) == -1

    nums = [1]
    assert bsearch_left_not_less_2(nums, 1) == 0

    nums = [1, 3, 3, 3, 3, 5, 6]
    assert bsearch_left_not_less_2(nums, 3) == 1

    nums = []
    assert bsearch_left_not_less_2(nums, 3) == -1

    nums = [1, 1, 3, 3, 3, 5, 6]
    assert bsearch_left_not_less_2(nums, 1) == 0


def test_bsearch_right_not_greater2():
    nums = [1, 2, 3, 3, 3, 5, 6]
    assert bsearch_right_not_greater2(nums, 3) == 4

    nums = [1]
    assert bsearch_right_not_greater2(nums, 3) == 0

    nums = [1]
    assert bsearch_right_not_greater2(nums, 1) == 0

    nums = [1, 3, 3, 3, 3, 3, 3]
    assert bsearch_right_not_greater2(nums, 3) == 6

    nums = []
    assert bsearch_right_not_greater2(nums, 3) == -1

    nums = [1, 1, 3, 3, 3, 5, 6]
    assert bsearch_right_not_greater2(nums, 1) == 1


def test_bsearch_in_cycle_order_array():
    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array(nums, 6) == 2

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array(nums, 5) == 1

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array(nums, 4) == 0

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array(nums, 1) == 3

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array(nums, 2) == 4

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array(nums, 3) == 5

    nums = [1, 2, 3, 4, 5, 6]
    assert bsearch_in_cycle_order_array(nums, 3) == 2

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array(nums, 8) == -1

    nums = [8, 9, 2, 3, 4]
    assert bsearch_in_cycle_order_array(nums, 9) == 1


def test_bsearch_in_cycle_order_array_by_recurse():
    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array_by_recurse(nums, 6) == 2

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array_by_recurse(nums, 5) == 1

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array_by_recurse(nums, 4) == 0

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array_by_recurse(nums, 1) == 3

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array_by_recurse(nums, 2) == 4

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array_by_recurse(nums, 3) == 5

    nums = [1, 2, 3, 4, 5, 6]
    assert bsearch_in_cycle_order_array_by_recurse(nums, 3) == 2

    nums = [4, 5, 6, 1, 2, 3]
    assert bsearch_in_cycle_order_array_by_recurse(nums, 8) == -1

    nums = [8, 9, 2, 3, 4]
    assert bsearch_in_cycle_order_array_by_recurse(nums, 9) == 1


def test_bsearch_in_cycle_order_array_2():
    nums = [2, 5, 6, 0, 0, 1, 2]
    assert bsearch_in_cycle_order_array_2(nums, 0) is True

    nums = [2, 5, 6, 0, 0, 1, 2]
    assert bsearch_in_cycle_order_array_2(nums, 2) is True

    nums = [2, 5, 6, 0, 0, 1, 2]
    assert bsearch_in_cycle_order_array_2(nums, 1) is True

    nums = [2, 5, 6, 0, 0, 1, 2]
    assert bsearch_in_cycle_order_array_2(nums, 5) is True

    nums = [2, 5, 6, 0, 0, 1, 2]
    assert bsearch_in_cycle_order_array_2(nums, 6) is True

    nums = [2, 5, 6, 0, 0, 1, 2]
    assert bsearch_in_cycle_order_array_2(nums, 8) is False
