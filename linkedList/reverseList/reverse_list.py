"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
"""
from linkedList.list_node import ListNode
from typing import List, Optional


class Solution:
    def reverse_list(self, head: ListNode) -> Optional[ListNode]:
        """使用临时变量，迭代方法反转链表"""
        if head is None:
            return None
        next_node = head.next
        head.next = None
        a = head
        while next_node is not None:
            tmp = next_node.next
            next_node.next = a
            a = next_node
            next_node = tmp
        return a

    def reverse_list_2(self, head: ListNode) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        while curr_node is not None:
            tmp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = tmp
        return prev_node

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

    def reverse_list_by_recurse(self, head: ListNode) -> Optional[ListNode]:
        """递归公式：head.next.next = head, new_head = recurse(head) """
        if head is None or head.next is None:
            return head
        new_head = self.reverse_list_by_recurse(head.next)
        head.next.next = head
        head.next = None
        return new_head


"""
使用迭代和递归两个方法。
迭代使用前后两个指针，依次更改指针方向。时间复杂度：O（n）,空间复杂度：O(1)
递归：考虑当前节点以后的链表都已经排好序后，如何反转列表。每次递归，都返回相同的最后一个节点。时间复杂度：n,空间复杂度：n，栈空间

"""