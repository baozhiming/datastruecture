from tree.node import Node


import queue
class Solution:
    def maxDepth(self, root: Node) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth2(self, root: Node) -> int:
        que = queue.Queue()
        if root is None:
            return 0
        que.put((root, 1))
        levels = set()
        high = 0
        while not que.empty():
            node, level = que.get()
            if level not in levels:
                levels.add(level)
                high += 1
            if node.left is not None:
                que.put((root.left, level+1))
            if node.right is not None:
                que.put((root.right, level+1))
        return high