class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: Node) -> Node:
        # 1. 找到head
        head = root
        while head.left is not None:
            head = head.left
        print(head.val)
        self.change_point(root)
        print(head.val)
        while root.right is not None:
            root = root.right
        head.left = root
        root.right = head
        return head

    def change_point(self, root):
        if root is None:
            return
        self.change_point(root.left)
        self.change_point(root.right)
        predecessor_node = root.left
        while predecessor_node is not None and predecessor_node.right is not None:
            predecessor_node = predecessor_node.right
        root.left = predecessor_node
        if predecessor_node is not None:
            predecessor_node.right = root

        successor_node = root.right
        while successor_node is not None and successor_node.left is not None:
            successor_node = successor_node.left
        root.right = successor_node
        if successor_node is not None:
            successor_node.left = root
