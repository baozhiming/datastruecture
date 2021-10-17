"""
数组实现顺序队列会涉及到数组搬移，如何避免数组搬移？
循环队列
要注意的是循环队列需要浪费一个元素空间，不存储元素。
"""
from typing import Union, Optional


class CircularQueue:
    def __init__(self, n: int):
        self.array = []
        self.n = n
        self.head = 0
        self.tail = 0

    def enqueue(self, val: Union[str, int]) -> bool:
        if (self.tail + 1) % self.n == self.head:
            return False
        self.array.insert(self.tail, val)
        self.tail = (self.tail + 1) % self.n
        return True

    def dequeue(self) -> Optional[Union[int, str]]:
        if self.head == self.tail:
            return None
        tmp = self.array[self.head]
        self.head = (self.head + 1) % self.n
        return tmp
