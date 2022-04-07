#  实现62进制的加法，0-9 a-z A-Z分别对应十进制的0-61，实现abc+abcd的加法？
#  1Z + Z = 2Y； abc + abc = kmo；dabc + abc = dkmo

class Solution:
    sixty_two2ten = dict()
    ten2sixty_two = dict()
    def __init__(self):
        for i in range(10):
            Solution.sixty_two2ten[str(i)] = i
            Solution.ten2sixty_two[str(i)] = i
        for i in range(26):
            Solution.sixty_two2ten[chr(97 + i)] = i + 10
            Solution.ten2sixty_two[str(i + 10)] = chr(97 + i)
        for i in range(26):
            Solution.sixty_two2ten[chr(65 + i)] = i + 36
            Solution.ten2sixty_two[str(i + 36)] = chr(65 + i)

    def add(self, a: str, b: str):
        a_i, b_i = len(a) - 1, len(b) - 1
        c = ""
        JW = 0  # 标示进位
        while a_i >= 0 and b_i >= 0:
            if a[a_i] not in Solution.sixty_two2ten or b[b_i] not in Solution.sixty_two2ten:
                return "包含62进制以外的数字"
            tmp = Solution.sixty_two2ten[a[a_i]] + Solution.sixty_two2ten[b[b_i]] + JW
            if tmp <= 61:
                c = f"{Solution.ten2sixty_two[str(tmp)]}{c}"
                JW = 0
            else:
                c = f"{Solution.ten2sixty_two[str(tmp - 62)]}{c}"
                JW = 1
            a_i -= 1
            b_i -= 1

        while a_i >= 0:
            tmp = Solution.sixty_two2ten[a[a_i]] + JW
            if tmp <= 61:
                c = f"{Solution.ten2sixty_two[str(tmp)]}{c}"
                JW = 0
            else:
                c = f"{Solution.ten2sixty_two[str(tmp - 62)]}{c}"
                JW = 1
            a_i -= 1
        while b_i >= 0:
            tmp = Solution.sixty_two2ten[b[b_i]] + JW
            if tmp <= 61:
                c = f"{Solution.ten2sixty_two[str(tmp)]}{c}"
                JW = 0
            else:
                c = f"{Solution.ten2sixty_two[str(tmp - 62)]}{c}"
                JW = 1
            b_i -= 1

        if JW == 1:
            c = f"1{c}"
        return c


handler = Solution()
re = handler.add("Z", "Z")
print(re)
assert re == "1Y"

re = handler.add("1Z", "Z")
print(re)
assert re == "2Y"


re = handler.add("abc", "abc")
print(re)
assert re == "kmo"

re = handler.add("dabc", "abc")
print(re)
assert re == "dkmo"

