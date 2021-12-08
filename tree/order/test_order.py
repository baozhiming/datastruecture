from tree.order.order import preOrder, inOrder, postOrder, layerOrder
from tree.node import array2tree


def test_preOrder():
    nums = [4, 3, 5, 1, 6, 7, 4, 2]
    root = array2tree(nums)
    re = preOrder(root)
    assert re == "43126574"

    nums = [4, 3, 5, 1, 6, 7, 4, 2]
    root = array2tree(nums)
    re = inOrder(root)
    assert re == "21364754"

    nums = [4, 3, 5, 1, 6, 7, 4, 2]
    root = array2tree(nums)
    re = postOrder(root)
    assert re == "21637454"

    nums = [4, 3, 5, 1, 6, 7, 4, 2]
    root = array2tree(nums)
    re = layerOrder(root)
    assert re == "43516742"