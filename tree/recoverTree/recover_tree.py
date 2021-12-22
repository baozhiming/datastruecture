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
        pass



"""
方法1：中序遍历获得数组之后，数组的值是递增的。当有两个节点互换，对应的是，数组中两个节点互换。所以找到互换的两个值。通过找到的值，遍历树，交换值。
时间复杂度：O(n)
空间复杂度: O(n)

"""