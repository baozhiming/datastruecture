# 给你二叉搜索树的根节点 root ，该树中的两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,3,null,null,2]
# 输出：[3,1,null,null,2]
# 解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
#
#
#  示例 2：
#
#
# 输入：root = [3,1,4,null,null,2]
# 输出：[2,1,4,null,null,3]
# 解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
#
#
#
#  提示：
#
#
#  树上节点的数目在范围 [2, 1000] 内
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#
#
#  进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 614 👎 0


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        """
        def inOrder(node: Optional[TreeNode]):
            if node is None:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)

        array = inOrder(root)

        p = []
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                p.append(i)

        i, j = None, None
        if len(p) == 1:
            i = array[p[0]]
            j = array[p[0] + 1]
        elif len(p) == 2:
            i = array[p[0]]
            j = array[p[1]+1]
        else:
            pass

        def inOrderReplace(node: Optional[TreeNode]):
            if node is None:
                return
            if node.val == i:
                node.val = j
            elif node.val == j:
                node.val = i
            inOrderReplace(node.left)
            inOrderReplace(node.right)

        inOrderReplace(root)

    def recoverTree2(self, root: Optional[TreeNode]) -> None:
        stack = []
        new_root = root
        last_node, x, y = None, None, None
        while root is not None or len(stack) != 0:
            while root is not None:
                stack.append(root)
                root = root.left

            current = stack.pop()
            if last_node is not None and current is not None and last_node.val > current.val:
                if x is None:
                    x = last_node
                    y = current
                else:
                    y = current
                    break

            last_node = current
            root = current.right

        tmp = x.val
        x.val = y.val
        y.val = tmp


    def recoverTree3(self, root: Optional[TreeNode]) -> None:
        last_node = None
        x, y = None, None

        def find_predecessor(root: TreeNode):
            if root is None:
                return None
            if root.left is None:
                return None
            node = root.left
            while node.right is not None:
                if node.right == root:
                    return node
                node = node.right
            return node

        while root is not None:
            if root.left is not None:
                predecessor = find_predecessor(root)
                if predecessor.right != root:
                    predecessor.right = root
                    root = root.left
                else:
                    if last_node is not None and root is not None and last_node.val >= root.val:
                        if x is None:
                            x = last_node
                            y = root
                        else:
                            y = root
                            predecessor.right = None
                    last_node = root
                    predecessor.right = None
                    root = root.right
            else:
                if last_node is not None and root is not None and last_node.val >= root.val:
                    if x is None:
                        x = last_node
                        y = root
                    else:
                        y = root
                last_node = root
                root = root.right

        tmp = x.val
        x.val = y.val
        y.val = tmp


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    while True:
        try:
            line = "[1,3,null,null,2]"
            root = stringToTreeNode(line);

            ret = Solution().recoverTree3(root)

            out = treeNodeToString(root)
            if ret is not None:
                print("Do not return anything, modify root in-place instead.")
            else:
                print(out)
            break
        except StopIteration:
            break


if __name__ == '__main__':
    main()








"""
方法1：中序遍历获得数组之后，数组的值是递增的。当有两个节点互换，对应的是，数组中两个节点互换。所以找到互换的两个值。通过找到的值，遍历树，交换值。
时间复杂度：O(n)
空间复杂度: O(n)
方法2：中序遍历使用递归时，临时栈占用了O（n）的空间。所以可以使用栈手动模拟入栈出栈过程。
时间复杂度：(n)
空间复杂度：O(high) 和高度成正比
"""