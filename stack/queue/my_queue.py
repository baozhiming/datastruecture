"""
使用两个栈实现队列的基本操作, push pop peek empty
"""
from stack.list_stack import ArrayStack


class MyQueue:
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()
        self.head = None

    def push(self, val: int) -> None:
        self.stack1.push(val)
        if self.head is None:
            self.head = val

    def pop(self) -> int:
        if self.head is None:
            return -1
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        val = self.stack2.pop()
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        self.head = self.stack2.top()
        return val

    def peek(self) -> int:
        return self.head

    def empty(self) -> bool:
        return self.head is None


"""
实现思路，使用队列实现技巧中的画图举例法，使用两个栈，push时入stack1，要想先进先出，则pop时现将stack1的所有元素pop并且push到
stack2，这样便实现先进先出所以：
push：push到第一个栈
pop：若栈stack2非空，则直接pop stack2，否则，将stack1的元素全部出栈并入栈到stack2。pop stack2
时间复杂度：这里使用摊还分析法。假设stack1有k个元素,stack2为空，则pop 第一个元素需要k步（搬移k个元素到第二个栈），pop剩余
k-1个元素都是1步。所以pop k个元素，一共需要k次搬移与k次pop操作，摊还下来，pop每个元素只需常数时间。
空间复杂度：O(1)
不足：
我实现的这个方法中的属性head，维护了整个队列的队首元素，每次pop stack2的最后一个元素时，都需要重新搬移元素。
如果head只维护stack1的栈低元素，也就是stack2不为空，则队首元素为stack2的栈顶元素；若stack2为空，则队首元素为head。
"""
