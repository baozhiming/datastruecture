"""
使用数组实现顺序栈
"""
from typing import List, Optional, Union


class ArrayStack:
    def __init__(self):
        self.stack: List = []
        self.count = 0

    def push(self, data: Union[str, int]) -> bool:
        self.stack.append(data)
        self.count += 1
        return True

    def pop(self) -> Optional[Union[str, int]]:
        if self.count == 0:
            return None
        self.count -= 1
        return self.stack.pop(-1)

    def top(self) -> Optional[Union[str, int]]:
        if self.count == 0:
            return None
        return self.stack[-1]

    def is_empty(self) -> bool:
        return self.count == 0
