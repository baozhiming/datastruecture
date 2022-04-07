"""
删除链表倒数第n个节点
"""
from linkedList.list_node import ListNode
from typing import List, Optional


class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        dummy = ListNode()
        dummy.next = head
        prev_node = dummy
        curr_node = dummy
        for i in range(n):
            curr_node = curr_node.next
        while curr_node.next is not None:
            prev_node = prev_node.next
            curr_node = curr_node.next
        prev_node.next = prev_node.next.next
        return dummy.next

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
思路：要找倒数第k个节点，先使用前后指针定位前k个节点，滑动窗口，直到后指针位于最后一个节点，前节点就位于倒数第k个节点的前一个节点
时间复杂度：O(n)
空间复杂度：O(1)
"""