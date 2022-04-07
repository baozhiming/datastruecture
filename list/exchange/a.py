from typing import List


class Solution:
    def find(self, string) -> str:
        nums = []
        for i in string:
            if i not in nums:
                nums.append(i)
            else:
                nums.remove(i)
        return "".join(nums)


handler = Solution()
print(handler.find("cbddbb"))