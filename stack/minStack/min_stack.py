"""
设计一个支持push、pop、top的操作，并在常数时间内返回最小元素的栈
"""


class MinStack:

    def __init__(self):
        self.val_stack = []
        self.min_stack = []
        self.count = 0

    def push(self, val: int) -> None:
        self.val_stack.append(val)
        if self.count == 0:
            self.min_stack.append(val)
        else:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        self.count += 1
        return

    def pop(self) -> None:
        if self.count == 0:
            return None
        self.val_stack.pop()
        self.min_stack.pop()
        self.count -= 1
        return

    def top(self) -> int:
        if self.count == 0:
            return -1
        return self.val_stack[-1]

    def getMin(self) -> int:
        if self.count == 0:
            return -1
        return self.min_stack[-1]


"""
想到的思路：使用一个列表实现栈，另一个列表按照大小排序。push、pop操作的时间复杂度为O(n);整体的空间复杂度为O(n)，使用了额外的列表来存储有序数据
优化思路：
解1：思路：因为栈只在一端进行操作，所以只要栈顶数据不变，栈中其余的元素就不会变。依赖这个特性，占中每个元素都对应一个此时的栈中最小值。
使用辅助栈来存储每个栈中元素对应的最小值
push：大于辅助栈栈顶元素，则数据栈入数据，辅助栈入当前最小值，也就是栈顶元素；小于辅助栈栈顶元素，则数据栈入数据，辅助栈入新的最小值。
pop：pop数据栈的同时，pop辅助栈的栈顶元素
时间复杂度：push、pop和getMin都是O（1）
空间复杂度：O（n）
技巧思路：
如何不实用额外的空间实现？
使用变量存储最小值。栈中的元素为与最小值的差值。
假设最小值变量为min_val, 栈为stack
push：val大于min_val，则将val - min_val入栈，若val小于最小值min_val，则入栈元素为val - min_val入栈，min_val = val。
pop：如果栈顶元素diff大于等于0，则栈顶元素为min_val + diff，若栈顶元素diff小于0，则栈顶元素为min_val，将min_val恢复为min_val - diff
 
"""
