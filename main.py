""">>> calculate_row(matrixX[0], matrixY)
[24, 50]
[24, 50]
"""

import threading

matrixX = [[3, 7], [4, 1]]
matrixY = [[1, 5], [3, 5]]


def calculate_element(row, col):
    Z = 0

    for i, item in enumerate(row):
        Z += item * col[i]
    return Z


def calculate_row(rowX, matrixY):
    cols = [[row[i] for row in matrixY] for i in range(len(matrixY[0]))]
    Z = list(map(lambda a: calculate_element(rowX, a), cols))
    print(Z)
    return Z


for row in matrixX:
    threading.Thread(target=calculate_row, args=(row, matrixY)).start()


if __name__ == '__main__':
    import doctest
    doctest.testmod()


