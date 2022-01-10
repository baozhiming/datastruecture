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


# 请实现两个函数，分别用来序列化和反序列化二叉树。
#
#  你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字
# 符串反序列化为原始的树结构。
#
#  提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方
# 法解决这个问题。
#
#
#
#  示例：
#
#
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
#
#
#
#


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        que = queue.Queue()
        que.put(root)
        data = []
        while not que.empty():
            node = que.get()
            if node is not None:
                data.append(node.val)
                que.put(node.left)
                que.put(node.right)
            else:
                data.append(None)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = TreeNode(data[0])
        self.recurse(root, data, 0)
        return root

    def recurse(self, root: TreeNode, nums, i: int):
        if i + 1 >= len(nums) // 2:
            return
        root.left = TreeNode(nums[i * 2 + 1])
        root.right = TreeNode(nums[i * 2 + 2])
        self.recurse(root.left, nums, i * 2 + 1)
        self.recurse(root.right, nums, i * 2 + 2)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == "__main__":
    nums = [4, 3, 5, 1, 6, 7, 4]
    root = array2tree(nums)
    assert root.val == 4
    assert root.left.val == 3
    assert root.right.val == 5
    assert root.left.left.val == 1
