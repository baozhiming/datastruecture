"""
使用链表实现链式栈
"""
from linkedList.list_node import ListNode
from typing import Optional


class LinkedStack:
    def __init__(self):
        self.head = ListNode("")

    def push(self, val: str) -> bool:
        tmp = ListNode(val)
        tmp.next = self.head.next
        self.head.next = tmp
        return True

    def pop(self) -> Optional[str]:
        if self.head.next is None:
            return None
        val = self.head.next.val
        self.head.next = not self.head.next.next
        return val

    def __repr__(self):
        current = self.head.next
        nums = []
        while current:
            nums.append(current.val)
            current = current.next
        return " ".join([f"{num}" for num in nums])
