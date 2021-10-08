"""判断一个单链表是否是回文链表"""
from linkedList.list_node import list2linked_list, echo_linked_list, ListNode
from typing import List


class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        middle_node = self.middle_node(head)
        tail_node = self.reverse_list(middle_node)
        result = self.compare_palindrome(head, tail_node)
        head = self.recover_list(head, tail_node)
        return result

    def middle_node(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def compare_palindrome(self, l: ListNode, r: ListNode) -> bool:
        while l is not None and r is not None:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True

    def recover_list(self, l: ListNode, r: ListNode) -> ListNode:
        if l is None:
            return l
        r = self.reverse_list(r)
        head = l
        while l.next is not None:
            l = l.next
        l.next = r
        return head

    def is_palindrome_by_recurse(self, head: ListNode) -> bool:
        self.pre_node = head

        def check_palindrome(current_node: ListNode):
            if current_node is not None:
                if not check_palindrome(current_node.next):
                    return False
                if self.pre_node.val != current_node.val:
                    return False
                self.pre_node = self.pre_node.next
            return True
        return check_palindrome(head)


"""
思路：
1。 使用快慢指针找到中间节点
2。 反转链表
3。 对前后连个链表进行比较
4。 恢复链表
时间复杂度：O（n）
空间复杂度：原地算法
思路：使用递归的方法：递归外的指针向右移动，递归最后一个节点之后，递归内的指针会向左移动。反向迭代和外指针双向迭代。
"""