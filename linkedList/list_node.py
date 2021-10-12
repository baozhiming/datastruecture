from typing import List, Optional, Union


class ListNode:
    def __init__(self, val: Union[str, int] = 0, next=None):
        self.val = val
        self.next = next


def list2linked_list(nums: List[int]) -> Optional[ListNode]:
    """ 数组转换为链表"""
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    tmp = head
    for i in range(1, len(nums)):
        tmp.next = ListNode(nums[i])
        tmp = tmp.next
    return head


def echo_linked_list(head: Optional[ListNode]):
    if head is None:
        return "None"
    return f"{head.val} -> " + echo_linked_list(head.next)
