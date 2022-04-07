"""
0-1背包问题。背包重量为W，n个物品，将物品装入背包，使得装入的重量最大？
贪心算法得不到最优解
如何得到最优解？
"""
from typing import List


max_weight = -1


def f(i: int, cw: int, array: List, w: int):
    """
    :param i: 第几个物品
    :param cw:  当前的重量
    :param array: 物品列表
    :param w: 背包重量
    :return:
    """
    global max_weight
    if i == len(array) or cw == w:
        if cw > max_weight:
            max_weight = cw
        return
    f(i+1, cw, array, w)
    if cw + array[i] <= w:
        f(i+1, cw+array[i], array, w)


# 上面的回溯算法可以枚举所有的情况，求最大重量。通过递归树可以判断，有很多重复计算的部分，可以用哈希或者二维数组来作为备忘录。提升效率


def f_with_dynamic(array: List, w: int):
    """
      使用动态规划求解
    :param i:
    :param cw:
    :param array:
    :param w:
    :return:
    """
    global max_weight
    # 动态规划每一层都是根据上一层的结果来计算本层的结果。所以第一层单独处理，哨兵
    # states = [[0] * (w + 1)] * len(array)  这个生成是不对的。
    states = [[0 for _ in range(w+1)] for _ in range(len(array))]
    states[0][0] = 1
    if array[0] <= w:
        states[0][array[0]] = 1
    for i in range(1, len(array)):
        for j in range(w + 1):  # 不放入第i个物品
            if states[i-1][j] == 1:
                states[i][j] = 1
        for j in range(w-array[i]+1):   # 放入第i个物品
            if states[i-1][j] == 1:
                states[i][j + array[i]] = 1

    for j in range(w, -1, -1):
        if states[len(array)-1][j] == 1:
            max_weight = j
            break


# 上面的算法就是动态规划的例子，降低了时间复杂度，为n*w，但是空间复杂度也上升了。所以优化空间复杂度
def f_with_dynamic_low_space(array: List, w: int):
    """
    优化上面的动态规划，用一个数组保存状态
    :param array:
    :param w:
    :return:
    """
    global max_weight
    states = [0 for _ in range(w + 1)]
    states[0] = 1
    if array[0] <= w:
        states[array[0]] = 1
    for i in range(1, len(array)):
        for j in range(w-array[i], -1, -1):
            if states[j] == 1:   # 不选择此商品的情况已经不用考虑了。
                states[j + array[i]] = 1

    for j in range(w, -1, -1):
        if states[w] == 1:
            max_weight = j
            break


# f(0, 0, [2, 2, 4, 6, 3], 9)
# print(max_weight)

f_with_dynamic_low_space([2, 2, 4, 6, 3], 9)
print(max_weight)

