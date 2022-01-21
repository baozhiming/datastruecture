"""
使用数组实现队列
"""
from typing import Union, Optional


class ArrayQueue:
    def __init__(self, n: int = 10):
        self.array = []
        self.n = n
        self.head = 0
        self.tail = 0

    def enqueue(self, val: Union[str, int]) -> bool:
        """入队，当队满的时候，需要搬移数据"""
        if self.tail == self.n:
            if self.head == 0:
                return False
            for i in range(self.head, self.tail):
                self.array[i - self.head] = self.array[i]
            self.tail = self.tail - self.head
            self.head = 0

        # 要注意python的列表是没有提前申请内存的，所以入队时不能直接安扎索引赋值；当发生数据搬移时，不能直接使用append
        self.array.insert(self.tail, val)
        self.tail += 1
        return True

    def dequeue(self) -> Optional[Union[str, int]]:
        if self.head == self.tail:
            return None
        re = self.array[self.head]
        self.head += 1
        return re

    def __repr__(self) -> str:
        return " ".join([i for i in self.array[self.head : self.tail]])
