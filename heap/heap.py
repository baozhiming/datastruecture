"""
实现一个堆
"""
from typing import Union, List


class MyHeap:
    """大顶堆"""
    def __init__(self):
        self.__heap = list()
        self.__count = 0

    def add(self, val: Union[str, int]):
        self.__heap.append(val)
        i = len(self.__heap) - 1
        father = (i - 1) // 2
        while father >= 0 and self.__heap[i] > self.__heap[father]:
            self.swap(self.__heap, i, father)
            i = father
            father = (i - 1) // 2

    def remove_max(self):
        re = self.__heap[0]
        self.__heap[0] = self.__heap.pop()
        self.heapify()
        return re

    def heapify(self):
        i = 0
        while True:
            if i * 2 + 2 < len(self.__heap):
                max_child = i * 2 + 1 if self.__heap[i * 2 + 1] > self.__heap[i * 2 + 2] else i * 2 + 2
            elif i * 2 + 1 < len(self.__heap):
                max_child = i * 2 + 1
            else:
                max_child = None

            if max_child is None or self.__heap[i] > self.__heap[max_child]:
                break
            self.swap(self.__heap, i, max_child)

            i = max_child

    def swap(self, nums: List, i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def print(self):
        print(self.__heap)


if __name__ == "__main__":
    heap = MyHeap()
    heap.add(8)
    heap.add(9)
    heap.add(10)
    heap.add(3)
    heap.add(11)
    heap.add(2)
    heap.print()
    print(heap.remove_max())
    heap.print()
