"""
使用链表实现队列，链式队列
"""
from typing import Union, Optional
from linkedList.list_node import ListNode


class LinkedQueue:
    def __init__(self, n: int):
        self.head = ListNode()
        self.n = n
        self.count = 0
        self.tail = self.head

    def enqueue(self, val: Union[str, int]) -> bool:
        if self.count == self.n:
            return False
        self.tail.next = ListNode(val)
        self.count += 1
        self.tail = self.tail.next

    def dequeue(self) -> Optional[Union[str, int]]:
        if self.count == 0:
            return None
        re = self.head.next.val
        self.head.next = self.head.next.next
        self.count -= 1
        return re
