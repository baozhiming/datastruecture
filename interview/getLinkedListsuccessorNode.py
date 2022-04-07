from typing import List, Optional


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def list2linkedList(array: List) -> Optional[Node]:
    if not array:
        return None
    head = Node(array[0])
    cur = head
    for i in range(1, len(array)):
        cur.next = Node(array[i])
        cur = cur.next
    return head


class Solution:
    def getProSuccessNode(self, head: Node, val: int) -> int:
        duck_node = Node(-1)
        duck_node.next = head
        curr_node = head
        while curr_node is not None:
            if curr_node.val == val:
                return duck_node.val
            curr_node = curr_node.next
            duck_node = duck_node.next
        return -1


handler = Solution()
input = [3, 4, 5, 6, 7, 8, 9]
linkedlist = list2linkedList(input)
re = handler.getProSuccessNode(linkedlist, 5)
print(re)
assert re == 4

re = handler.getProSuccessNode(linkedlist, 9)
print(re)
assert re == 8


input = []
linkedlist = list2linkedList(input)
re = handler.getProSuccessNode(linkedlist, 5)
print(re)
assert re == -1


input = [1]
linkedlist = list2linkedList(input)
re = handler.getProSuccessNode(linkedlist, 5)
print(re)
assert re == -1


input = [1]
linkedlist = list2linkedList(input)
re = handler.getProSuccessNode(linkedlist, 1)
print(re)
assert re == -1


input = [1, 2]
linkedlist = list2linkedList(input)
re = handler.getProSuccessNode(linkedlist, 2)
print(re)
assert re == 1
