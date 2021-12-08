from typing import Union, List, Optional


class Node:
    def __init__(self, val: Union[str, int] = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array2tree(array: List) -> Optional[Node]:
    if not array:
        return None
    for i in range(len(array)):
        array[i] = Node(array[i])
        if i == 0:
            continue
        if i % 2 == 1:
            array[i // 2].left = array[i]
        else:
            array[(i - 1) // 2].right = array[i]
    return array[0]


if __name__ == "__main__":
    nums = [4, 3, 5, 1, 6, 7, 4]
    root = array2tree(nums)
    assert root.val == 4
    assert root.left.val == 3
    assert root.right.val == 5
    assert root.left.left.val == 1
