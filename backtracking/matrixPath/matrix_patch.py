# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
#  例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
#
#
#
#
#
#  示例 1：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCCED"
# 输出：true
#
#
#  示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#
#
#
#
#  提示：
#
#
#  1 <= board.length <= 200
#  1 <= board[i].length <= 200
#  board 和 word 仅由大小写英文字母组成
#
#
#
#
#  注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
#  Related Topics 数组 回溯 矩阵 👍 569 👎 0
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board and not word:
            return True
        if not board:
            return False
        if not word:
            return True
        exist_word = False
        rows, cols = len(board), len(board[0])

        def backtracking(row: int, col: int, word_index: int, states: List[List[int]]):
            nonlocal board, rows, cols, word, exist_word
            if exist_word is True:
                return
            if board[row][col] != word[word_index]:
                return
            if word_index == len(word) - 1:
                exist_word = True
                return
            if row > 0 and board[row - 1][col] == word[word_index + 1] and states[row - 1][col] != 1:
                states[row][col] = 1
                backtracking(row - 1, col, word_index + 1, states)
                states[row][col] = 0

            if row < rows - 1 and board[row + 1][col] == word[word_index + 1] and states[row + 1][col] != 1:
                states[row][col] = 1
                backtracking(row + 1, col, word_index + 1, states)
                states[row][col] = 0

            if col > 0 and board[row][col - 1] == word[word_index + 1] and states[row][col - 1] != 1:
                states[row][col] = 1
                backtracking(row, col - 1, word_index + 1, states)
                states[row][col] = 0

            if col < cols - 1 and board[row][col + 1] == word[word_index + 1] and states[row][col + 1] != 1:
                states[row][col] = 1
                backtracking(row, col + 1, word_index + 1, states)
                states[row][col] = 0

        for i in range(rows):
            for j in range(cols):
                states = [[0 for i in range(cols)] for _ in range(rows)]
                backtracking(i, j, 0, states)
                if exist_word is True:
                    return exist_word

        return exist_word

    def exist_optimizatin(self, board: List[List[str]], word: str) -> bool:
        """
        简化写法，简化主要利用了or运算符可，如果第一个为True，则不会计算后面的表达式。所以将所有的递归放到or中
        """
        if not board and not word:
            return True
        if not board:
            return False
        if not word:
            return True
        exist_word = False
        rows, cols = len(board), len(board[0])

        def backtracking(row: int, col: int, word_index: int, states: List[List[int]]):
            nonlocal board, rows, cols, word, exist_word
            if row < 0 or row == rows or col < 0 or col == cols: return False
            if board[row][col] != word[word_index]: return False
            if states[row][col] == 1: return False
            if word_index == len(word) - 1:
                return True

            states[row][col] = 1
            re = (backtracking(row - 1, col, word_index + 1, states) or
                  backtracking(row + 1, col, word_index + 1, states) or
                  backtracking(row, col - 1, word_index + 1, states) or
                  backtracking(row, col + 1, word_index + 1, states))
            states[row][col] = 0
            return re

        for i in range(rows):
            for j in range(cols):
                states = [[0 for i in range(cols)] for _ in range(rows)]
                if backtracking(i, j, 0, states):
                    return True

        return False


handler = Solution()
re = handler.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
print(re)
assert re is True

re = handler.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "BCCED")
print(re)
assert re is True

re = handler.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "CCED")
print(re)
assert re is True

re = handler.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "BCCD")
print(re)
assert re is False

re = handler.exist([["a", "b"], ["c", "d"]], "abcd")
print(re)
assert re is False

"""
做这道题的时候，有两种情况没有考虑到，导致时间超时
1. 矩阵所有字符都一样。
没有添加58、59行，导致了即便找到了，还是会继续回溯
2。
没有添加89、90行。还是会重复回溯
"""

handler = Solution()
re = handler.exist_optimizatin([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
print(re)
assert re is True

re = handler.exist_optimizatin([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "BCCED")
print(re)
assert re is True

re = handler.exist_optimizatin([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "CCED")
print(re)
assert re is True

re = handler.exist_optimizatin([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "BCCD")
print(re)
assert re is False

re = handler.exist_optimizatin([["a", "b"], ["c", "d"]], "abcd")
print(re)
assert re is False

re = handler.exist_optimizatin([["a", "a"]], "aaa")
print(re)
assert re is False
