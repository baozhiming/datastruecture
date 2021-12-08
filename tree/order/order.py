from tree.node import Node
from typing import Union, Optional
from my_queue.linked_queue import LinkedQueue
import queue


def preOrder(root: Optional[Node]) -> str:
    if root is None:
        return ""
    return str(root.val) + preOrder(root.left) + preOrder(root.right)


def inOrder(root: Optional[Node]) -> str:
    if root is None:
        return ""
    return inOrder(root.left) + str(root.val) + inOrder(root.right)


def postOrder(root: Optional[Node]) -> str:
    if root is None:
        return ""
    return postOrder(root.left) + postOrder(root.right) + str(root.val)


def layerOrder(root: Optional[Node]) -> str:
    re = ""
    que = queue.Queue()
    que.put(root)
    while not que.empty():
        node = que.get()
        re += str(node.val)
        if node.left is not None:
            que.put(node.left)
        if node.right is not None:
            que.put(node.right)
    return re


def preOrderPrint(root: Optional[Node]):
    if root is None:
        return
    print(f"{root.val} -> ")
    preOrderPrint(root.left)
    preOrderPrint(root.right)


def inOrderPrint(root: Optional[Node]):
    if root is None:
        return
    inOrderPrint(root.left)
    print(f"{root.val} -> ")
    inOrderPrint(root.right)


def postOrderPrint(root: Optional[Node]):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(f"{root.val} ->")
