"""
使用数组实现顺序栈
"""
from typing import List, Optional


class ArrayStack:
    def __init__(self):
        self.stack: List = []
        self.count = 0

    def push(self, data: str) -> bool:
        self.stack.append(data)
        self.count += 1
        return True

    def pop(self) -> Optional[str]:
        if self.count == 0:
            return None
        self.count -= 1
        return self.stack.pop(-1)

    def is_empty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False
