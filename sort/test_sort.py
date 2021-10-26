from sort.bubble_sort import bubble_sort
from sort.select_sort import select_sort
from sort.insert_sort import insert_sort
from sort.merge_sort import merge_sort
from sort.quick_sort import quick_sort


def test_bubble_sort():
    nums = [4, 5, 6, 3, 2, 1]
    re = bubble_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [6, 5, 4, 3, 2, 1]
    re = bubble_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [1, 2, 3, 4, 5, 6]
    re = bubble_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [4, 5, 6, 2, 2, 1]
    re = bubble_sort(nums)
    assert re == [1, 2, 2, 4, 5, 6]

    nums = [4]
    re = bubble_sort(nums)
    assert re == [4]


def test_insert_sort():
    nums = [4, 5, 6, 3, 1, 2]
    re = insert_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [6, 5, 4, 3, 2, 1]
    re = insert_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [1, 2, 3, 4, 5, 6]
    re = insert_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [4, 5, 6, 2, 2, 1]
    re = insert_sort(nums)
    assert re == [1, 2, 2, 4, 5, 6]

    nums = [4]
    re = insert_sort(nums)
    assert re == [4]


def test_select_sort():
    nums = [4, 5, 6, 3, 1, 2]
    re = select_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [6, 5, 4, 3, 2, 1]
    re = select_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [1, 2, 3, 4, 5, 6]
    re = select_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [4, 5, 6, 2, 2, 1]
    re = select_sort(nums)
    assert re == [1, 2, 2, 4, 5, 6]

    nums = [4]
    re = select_sort(nums)
    assert re == [4]


def test_merge_sort():
    nums = [4, 5, 6, 3, 1, 2]
    re = merge_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [6, 5, 4, 3, 2, 1]
    re = merge_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [1, 2, 3, 4, 5, 6]
    re = merge_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [4, 5, 6, 2, 2, 1]
    re = merge_sort(nums)
    assert re == [1, 2, 2, 4, 5, 6]

    nums = [4]
    re = merge_sort(nums)
    assert re == [4]


def test_quick_sort():
    nums = [4, 5, 6, 3, 1, 2]
    re = quick_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [6, 5, 4, 3, 2, 1]
    re = quick_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [1, 2, 3, 4, 5, 6]
    re = quick_sort(nums)
    assert re == [1, 2, 3, 4, 5, 6]

    nums = [4, 5, 6, 2, 2, 1]
    re = quick_sort(nums)
    assert re == [1, 2, 2, 4, 5, 6]

    nums = [4]
    re = quick_sort(nums)
    assert re == [4]
