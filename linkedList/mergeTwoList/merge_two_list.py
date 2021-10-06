"""
合并两个有序的单链表，使合并之后的链表仍有序
"""

from linkedList.list_node import ListNode
from typing import List, Optional


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode()
        tmp = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        if l1 is not None:
            tmp.next = l1
        if l2 is not None:
            tmp.next = l2

        return head.next

    def merge_two_lists_by_recurse(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge_two_lists_by_recurse(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists_by_recurse(l1, l2.next)
            return l2

    @staticmethod
    def list2linked_list(nums: List[int]) -> Optional[ListNode]:
        """数组转换为链表"""
        if len(nums) == 0:
            return None
        head = ListNode(nums[0])
        tmp = head
        for i in range(1, len(nums)):
            tmp.next = ListNode(nums[i])
            tmp = tmp.next
        return head

    @staticmethod
    def echo_linked_list(head: Optional[ListNode]):
        if head is None:
            return "None"
        return f"{head.val} -> " + Solution.echo_linked_list(head.next)


"""
使用迭代和递归两个方法
迭代：依次比较头节点值。时间复杂度：O(n)， 空间复杂度：O(1)
递归：从头到尾递归。时间复杂度：O(n)， 空间复杂度：O(n)
"""