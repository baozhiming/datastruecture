# 检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。
#
#  如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。
#
#  注意：此题相对书上原题略有改动。
#
#  示例1:
#
#
#  输入：t1 = [1, 2, 3], t2 = [2]
#  输出：true
#
#
#  示例2:
#
#
#  输入：t1 = [1, null, 2, 4], t2 = [3, 2]
#  输出：false
#
#
#  提示：
#
#
#  树的节点数目范围为[0, 20000]。
#
#  Related Topics 树 深度优先搜索 二叉树 字符串匹配 哈希函数 👍 46 👎 0


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    MOD = 100007
    check = False
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 is None and t2 is None:
            return True
        elif t1 is None and t2 is not None:
            return False
        elif t1 is not None and t2 is None:
            return False
        if t1.val != t2.val:
            return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)
        same_left = self.checkSubTree(t1.left, t2.left)
        same_right = self.checkSubTree(t1.right, t2.right)
        if same_right and same_left:
            return True
        else:
            return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

    def checkSubTree2(self, t1: TreeNode, t2: TreeNode) -> bool:
        t2_hash = self.hash(t2)
        self.recurse(t1, t2_hash)
        return self.check

    def recurse(self, t1: TreeNode, t2_hash: int):
        if self.check is True:
            return 0
        if t1 is None:
            return 0
        left_hash = self.recurse(t1.left, t2_hash)
        right_hash = self.recurse(t1.right, t2_hash)
        t1_hash = (t1.val + left_hash * 31 + right_hash * 131) % self.MOD
        if t1_hash == t2_hash:
            self.check = True
        return t1_hash

    def hash(self, t: TreeNode) -> int:
        if t is None:
            return 0
        return (t.val + self.hash(t.left) * 31 + self.hash(t.right) * 131) % self.MOD


"""
思路一：暴力递归，以t1的每个节点为根结点，与t2比较。`
时间复杂度是 n * m
空间复杂度：1

思路2：题的关键词中有一个关键词是哈希函数。利用哈希函数，可以计算出t2的哈希值。然后计算t1每个节点作为根结点的哈希值，与t2的哈希值比较，来判断是否
拥有子树
问：在计算t1的哈希值时是否有冲突？
不需要散列表，哈希函数的除膜运算的除数可以无限大，冲突的概率很低，基本为0
如果冲突了就在计算一次hash值
使用树的后序遍历，从底向上的判断，如果不是子树，计算的值，继续供父节点使用。

时间复杂度：O(n + m)
空间复杂度：O(1)
"""