from typing import List


# 用来存放八皇后，索引是行，值是列
result = [-1 for i in range(8)]


def call8queens(row: int):
    if row == 8:
        print8queues()
        return
    for i in range(8):
        if isOk(row, i):
            result[row] = i
            # row += 1  第一遍写八皇后的时候，是这么写的，然后下一行是call8queens(row)。这个错误调试了很久。错误在于，在每一层递归的时候，计算确定了第row行放置Q到第i列之后，
            # 进行下一层递归之前，将row错误的计算成了下一行。每次递归回溯的时候，都计算错了行，计算成了一下行。
            # 定位了这么久的原因：debug没有开启递归栈信息，开启之后，在递归的过程中，看前面递归的栈中数据，发现不对。才定位到错误
            call8queens(row + 1)


def isOk(row: int, column: int):
    leftUp, rightUp = column - 1, column + 1
    for i in range(row-1, -1, -1):
        if result[i] == column:
            return False
        if result[i] != -1 and result[i] == leftUp:
            return False
        if result[i] != -1 and result[i] == rightUp:
            return False
        leftUp -= 1
        rightUp += 1
    return True


def print8queues():
    for i in range(len(result)):
        array = []
        for j in range(8):
            if result[i] == j:
                array.append("Q")
            else:
                array.append("*")
        print(" ".join(array))
    print("=================")


call8queens(0)
