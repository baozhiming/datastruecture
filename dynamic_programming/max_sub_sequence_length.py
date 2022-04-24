"""
最长递增子序列长度
有n个不同的数组序列，求最长的递增子序列长度。如2、9、3、6、5、1、7。最长递增子序列为2 3 5 7， 等于4
"""
from typing import List
import sys


class Solution:
    def max_length_by_backtracking(self, array: List) -> int:
        """
        回溯算法解决问题
        时间复杂度：对数据别的。2 ^ len(array)
        :param array:
        :return:
        """
        max_length = 0
        min_value = -sys.maxsize + 1

        def backtracking(i: int, cur_value: int, cur_len: int):
            nonlocal max_length, array
            if i == len(array):
                if cur_len > max_length:
                    max_length = cur_len
                return
            backtracking(i + 1, cur_value, cur_len)
            if array[i] > cur_value:
                backtracking(i + 1, array[i], cur_len + 1)

        backtracking(0, min_value, 0)
        return max_length

    def max_length_by_dynamic_programming(self, array: List) -> int:
        """
        动态规划求解
        时间复杂度：O(n ^ 2)
        :param array:
        :return:
        """
        if not array:
            return 0
        states = [[1 for i in range(len(array))] for _ in range(len(array))]
        for i in range(1, len(array)):
            # 不选择
            for j in range(i):
                states[i][j] = states[i-1][j]
            # 选择
            for j in range(i):
                if array[i] > array[j] and states[i][i] < states[i][j] + 1:
                    states[i][i] = states[i][j] + 1
        count = 1
        for i in range(len(array)):
            if states[len(array)-1][i] > count:
                count = states[len(array)-1][i]
        return count


fex = " 的最长递增子序列长度为 "
handle = Solution()
re = handle.max_length_by_backtracking([2, 9, 3, 6, 5, 1, 7])
print(f"[2, 9, 3, 6, 5, 1, 7]{fex}{re}")
assert re == 4

array = [2, 9, 3, 6, 5, 1, 7, 10]
re = handle.max_length_by_backtracking(array)
print(f"{array}{fex}{re}")
assert re == 5

array = [9, 2]
re = handle.max_length_by_backtracking(array)
print(f"{array}{fex}{re}")
assert re == 1

array = [9]
re = handle.max_length_by_backtracking(array)
print(f"{array}{fex}{re}")
assert re == 1

array = []
re = handle.max_length_by_backtracking(array)
print(f"{array}{fex}{re}")
assert re == 0


print("======动态规划")
fex = " 的最长递增子序列长度为 "
handle = Solution()
re = handle.max_length_by_dynamic_programming([2, 9, 3, 6, 5, 1, 7])
print(f"[2, 9, 3, 6, 5, 1, 7]{fex}{re}")
assert re == 4

array = [2, 9, 3, 6, 5, 1, 7, 10]
re = handle.max_length_by_dynamic_programming(array)
print(f"{array}{fex}{re}")
assert re == 5

array = [9, 2]
re = handle.max_length_by_dynamic_programming(array)
print(f"{array}{fex}{re}")
assert re == 1

array = [9]
re = handle.max_length_by_dynamic_programming(array)
print(f"{array}{fex}{re}")
assert re == 1

array = []
re = handle.max_length_by_dynamic_programming(array)
print(f"{array}{fex}{re}")
assert re == 0

array = [7, 7, 7, 7, 7, 7, 7]
re = handle.max_length_by_dynamic_programming(array)
print(f"{array}{fex}{re}")
assert re == 1


array = [10, 9, 2, 5, 3, 7, 101, 5]
re = handle.max_length_by_dynamic_programming(array)
print(f"{array}{fex}{re}")
assert re == 4


"""
这道题，使用回溯算法求解，画出状态转移树之后，状态为f(i, cur_max_value, cur_len), 
其中i为到达了下标为i的元素，还没考虑此元素；
cur_max_value代表了当前的最大值
cur_len代表了当前的长度。
所以多阶段决策，其中的多阶段一共有数组长度个阶段。这个很好理解，作为行
但是列要取什么值呢？取当前的值？还是当前的长度？
其实都可以，当列取当前值时，状态转移表存储的就是当前最大的长度。从状态树中可以看出含义为：到达某个元素时，要取长度最长的子序列。
当列取长度时，状态表中存储的是当前最大值。从状态树中看出的含义为: 子序列的长度相同时，要使得当前的最大值尽可能的小，让后面的可选项更多。

"""