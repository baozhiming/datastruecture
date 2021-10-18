"""
输入一个字符串，实现一个计算器计算结果
字符串包含：+ - （ ） ' '
"""
from stack.list_stack import ArrayStack


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return -1
        stack1 = ArrayStack()
        stack2 = ArrayStack()
        is_new_word = True
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            elif s[i] not in ('+', '-', ')', '('):
                if is_new_word:
                    stack1.push(int(s[i]))
                    is_new_word = False
                else:
                    stack1.push(stack1.pop() * 10 + int(s[i]))
                continue
            elif s[i] == '(':
                stack2.push(s[i])
                is_new_word = True
            elif s[i] == '+' or s[i] == '-':
                is_new_word = True
                if stack2.is_empty() or stack2.top() == '(':
                    stack2.push(s[i])
                elif stack2.top() == '+':
                    stack1.push(stack1.pop() + stack1.pop())
                    stack2.pop()
                    stack2.push(s[i])
                elif stack2.top() == '-':
                    a = stack1.pop()
                    b = stack1.pop()
                    stack1.push(b - a)
                    stack2.pop()
                    stack2.push(s[i])
            elif s[i] == ')':
                is_new_word = True
                while stack2.top() != '(':
                    case = stack2.pop()
                    if case == '+':
                        stack1.push(stack1.pop() + stack1.pop())
                    elif case == '-':
                        a = stack1.pop()
                        b = stack1.pop()
                        stack1.push(b - a)
                stack2.pop()
        if not stack2.is_empty():
            while not stack2.is_empty():
                case = stack2.pop()
                if case == '+':
                    stack1.push(stack1.pop() + stack1.pop())
                elif case == '-':
                    a = stack1.pop()
                    b = stack1.pop()
                    stack1.push(b - a)
        return stack1.pop()

    def calculate1(self, s: str) -> int:
        sign = 1
        stack = [1]
        ret = 0

        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = stack[-1]
                i += 1
            elif s[i] == '-':
                sign = -stack[-1]
                i += 1
            elif s[i] == '(':
                stack.append(sign)
                i += 1
            elif s[i] == ')':
                stack.pop()
                i += 1
            else:
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += sign * num
        return ret


"""
思路：使用两个栈，栈1压入数字，栈2压入符号，左括号直接入栈，每次入计算符号，判断栈顶是否是左括号，如果是，则不计算。如果是右括号，
则计算到左括号。注意的是要考虑数字为多位数。TODO 这个思路如何处理负数，没有想好
官方思路：
考虑人计算表达式是如何计算的，是把每个括号展开，在进行计算。展开括号的时候，可以看当前数字处于几个括号之内，根据每个括号前面的正负号，便可以判定当前
字符的符号。
有了这个思路，可以知道到每个括号都对应一个正负号，达某一个括号时，括号前面的符号最终应该是正还是负也便知道了。此时还需要一个标识符，如果当前符号是
加号，则下一个数字的正负号为括号前对应的最终正负号；如果当前符号是减号，则下一个数字的正负号为括号前对应的最终正负号的相反数。当遇到右括号时，
便可以pop栈顶元素。
注意：当没有括号时，所有数字前的符号就是其本身，不需要转换。所以可以设置栈顶元素和标识符为1。
时间复杂度为：n，需要迭代
空间复杂度为：n，用到了栈，且字符随机取值
"""
