"""
给定s和t两个字符串，当它们分别被输入到空白的编辑器后，判断两个字符串是否相等。#表示回退键，退格字符
"""
from stack.list_stack import ArrayStack


class Solution:
    def back_space_compare(self, s: str, t: str) -> bool:
        stack1 = ArrayStack()
        stack2 = ArrayStack()
        for i in s:
            if i != '#':
                stack1.push(i)
            else:
                if not stack1.is_empty():
                    stack1.pop()
        for i in t:
            if i != '#':
                stack2.push(i)
            else:
                if not stack2.is_empty():
                    stack2.pop()
        while not stack1.is_empty() and not stack2.is_empty():
            if stack1.pop() != stack2.pop():
                return False
        if not stack1.is_empty() or not stack2.is_empty():
            return False
        return True

    def back_space_compare_by_one_space_false(self, s: str, t: str) -> bool:
        """进阶"""
        val1 = ""
        val2 = ""
        s_point, t_point = 0, 0
        while s_point < len(s) or t_point < len(t):
            if s_point < len(s):
                if s[s_point] == '#':
                    if val1 != "":
                        val1 = ""
                    s_point += 1
                    continue
                else:
                    if val1 == "":
                        val1 = s[s_point]
                        s_point += 1
                        continue
            if t_point < len(t):
                if t[t_point] == '#':
                    if val2 != "":
                        val2 = ""
                    t_point += 1
                    continue
                else:
                    if val2 == "":
                        val2 = t[t_point]
                        t_point += 1
                        continue
            if val1 == val2:
                val1, val2 = '', ''
            else:
                return False
        return val1 == val2


    def back_space_compare_by_one_space_true(self, s: str, t: str) -> bool:
        """进阶"""
        s_point, t_point = len(s) - 1, len(t) - 1
        s_skip, t_skip = 0, 0
        while s_point >= 0 and t_point >= 0:
            if s[s_point] != '#' and t[t_point] != '#':
                if s_skip != 0:
                    s_point -= 1
                    s_skip -= 1
                    continue
                if t_skip != 0:
                    t_point -= 1
                    t_skip -= 1
                    continue
                if s[s_point] != t[t_point]:
                    return False
                s_point -= 1
                t_point -= 1
            elif s[s_point] == '#' or t[t_point] == '#':
                if s[s_point] == '#':
                    s_skip += 1
                    s_point -= 1
                if t[t_point] == '#':
                    t_skip += 1
                    t_point -= 1
                continue
        if s_point >= 0:
            while s_point >= 0:
                if s_skip == 0 and s[s_point] != '#':
                    return False
                elif s[s_point] == '#':
                    s_skip += 1
                elif s_skip != 0:
                    s_skip -= 1
                s_point -= 1
        if t_point >= 0:
            while t_point >= 0:
                if t_skip == 0 and t[t_point] != '#':
                    return False
                elif t[t_point] == '#':
                    t_skip += 1
                elif t_skip != 0:
                    t_skip -= 1
                t_point -= 1
        return True


"""
解法一：思路：使用两个栈，将两个字符串分别入栈，入到#号则出栈。比较两个栈的元素是否相等
时间复杂度：n，空间复杂度：n
进阶：尝试使用时间复杂度为O（n），空间复杂度为O（1）的方法实现
自己想到的方法：先到的是将两个栈的长度是为1。使用指针，只要后一个元素不是#，则比较占中的两个元素。这个方法在back_space_compare_by_one_space实现了，
不过这个方法是错误的。对于ab##的用例，此方法将失败。在不确定后面有几个#好的前提下，是不能比较的。这个方法是错误答案。在这里记下。
官方答案：重点思路为：#只影响前面的字符，不影响后面的字符。 根据这个想法，可以推出使用倒叙的遍历。用变量记录#号的个数，以跳过前面的字符。
双指针遍历两个字符串s，t。：
  如果skip为0，则不需要忽略数字
  如果skip不为0，则忽略字符，skip -1
直到找到两个字符串都不用删除的元素，进行比较。
"""