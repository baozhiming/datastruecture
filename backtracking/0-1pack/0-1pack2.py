"""
0-1背包升级问题：不同重量，不同价值，不能分割。最大重量情况下，价值最大
"""


maxV = -1
items = [2, 2, 4, 6, 3]
values = [3, 4, 8, 9, 6]


def f(i: int, cw: int, cv: int, w: int):
    """
    回溯算法
    :param i: 第几个物品
    :param cw: 当前重量
    :param cv: 当前价值
    :param w: 背包重量
    :return:
    """
    global maxV
    if i == len(items) or cw == w:
        if cv > maxV:
            maxV = cv
        return
    f(i+1, cw, cv, w)
    if cw + items[i] <= w:
        f(i+1, cw+items[i], cv+values[i], w)


# 回溯算法使用的枚举，虽然可以找到最优解，但是效率慢。这里先画出递归树，在分析


def f_dynamic(w: int):
    """
    动态规划：使用动态规划方法来求解。通过递归树发现，当行数和重量相同时，只取价值最大的情况就可以了。
    :param i:
    :param cw:
    :param cv:
    :param w:
    :return:
    """
    global maxV
    states = [[-1 for i in range(w+1)] for i in range(len(items))]
    states[0][0] = 0
    if items[0] <= w:
        states[0][items[0]] = values[0]
    for i in range(1, len(items)):
        for j in range(w+1):  # 不装入
            if states[i-1][j] != -1:
                states[i][j] = states[i-1][j]
        for j in range(w-items[i]+1):   # 装入
            if states[i-1][j] != -1 and values[i] + states[i-1][j] > states[i][j+items[i]]:
                states[i][j+items[i]] = values[i] + states[i-1][j]

    for j in range(w, -1, -1):
        if states[len(items)-1][j] != -1:
            maxV = states[len(items)-1][j]
            break


# 上述的动态规划其实还可以继续优化，降低空间复杂度.

f_dynamic(9)
print(maxV)


