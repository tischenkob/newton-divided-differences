from numpy import shape, zeros


def divdif(x, y):
    size = shape(y)[0]
    table = zeros([size, size])
    table[:, 0] = y  # первая колонна таблицы = y

    for j in range(1, size):
        for i in range(size - j):
            dif_y = table[i + 1][j - 1] - table[i][j - 1]
            dif_x = x[i + j] - x[i]
            table[i][j] = dif_y / dif_x

    return table[0]  # возвращаем первую строку


def poly_from(b, xi):
    polynom = ""
    for i in range(len(b)):
        polynom += "+ b[" + str(i) + "] "
        for j in range(i):
            polynom += " * (x - xi[" + str(j) + "]) "

    def compute(x):
        b
        xi
        return eval(polynom)

    return compute

