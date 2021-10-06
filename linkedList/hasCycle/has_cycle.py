"""
检测链表是否存在环
"""
from linkedList.list_node import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


"""
思想：使用快慢指针，如果快慢指针相遇，则存在环。龟兔赛跑
为何存在环，快慢指针一定会相遇？当快慢指针都进入环之后，想象环为一条直线，快指针在慢指针后面。则两指针间距离越来越短，无论之间相隔几个
节点，都会相遇。如果量指针挨着，则下一步相遇。如果间隔一个节点，下下步相遇。
时间复杂度：O()
"""
