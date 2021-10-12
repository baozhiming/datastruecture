"""
检测括号是否是有效的
"""
from stack.list_stack import ArrayStack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = ArrayStack()
        for i in s:
            if i == '[' or i == '{' or i == '(':
                stack.push(i)
            elif i == ']':
                stack_top = stack.pop()
                if stack_top == '[':
                    continue
                else:
                    return False
            elif i == '}':
                stack_top = stack.pop()
                if stack_top == '{':
                    continue
                else:
                    return False
            elif i == ')':
                stack_top = stack.pop()
                if stack_top == '(':
                    continue
                else:
                    return False
        return stack.is_empty()



"""
时间复杂度： O(n)
空间复杂度： O(n)
"""
