"""
返回单链表的中间节点
"""
from linkedList.list_node import ListNode
from typing import Optional


class Solution:
    def middle_node(self, head: ListNode) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


"""
时间复杂度：O(n)
空间复杂度：O(1)
"""