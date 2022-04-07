from typing import List


class Solution:
    def swap(self, a: str, b: str):
        i, j = 0, 0
        re = []
        while i < len(a):
            if a[i] == b[i]:
                i += 1
                continue
            same_index = -1
            for k in range(i+1, len(b)):
                if b[k] == a[i]:
                    same_index = k
                    break
            if same_index != -1:
                a, b = self.one_swap(a, b, len(a) - 1, same_index)
                a, b, = self.one_swap(a, b, len(a) - 1, i)
                re.append((len(a) - 1, same_index))
                re.append((len(a) - 1, i))
                i += 1
                continue
            else:
                for k in range(i+1, len(a)):
                    if a[k] == a[i]:
                        same_index = k
                        break
                if same_index != -1:
                    a, b = self.one_swap(a, b, same_index, i)
                    re.append((same_index, i))
                    i += 1
                else:
                    break
        return re

    def one_swap(self, a, b, i, j):
        tmp = a
        a = a[:i] + b[j] + a[i+1:]
        b = b[:j] + tmp[i] + b[j+1:]
        return a, b


handler = Solution()
print(handler.swap("souse", "houhe"))