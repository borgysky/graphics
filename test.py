import numpy as np
def test():
    coeff = 2
    coords = [[0 for x in range(2)] for y in range(2)]
    coords[0][0], coords[0][1], coords[1][0], coords[1][1] = 1, 2, 3, 4
    mul_coeff = [[0 for x in range(2)] for y in range(2)]
    mul_coeff[0][0], mul_coeff[0][1], mul_coeff[1][0], mul_coeff[1][1] = coeff, 0, 0, coeff
    res = np.matmul(coords, mul_coeff)
    for row in res:
        print(row)

test()

x = [[0 for x in range(2)] for y in range(2)]
x[0][0], x[0][1], x[1][0], x[1][1] = 4, 2, 9, 0
y = [[0 for x in range(2)] for y in range(2)]
y[0][0], y[0][1], y[1][0], y[1][1] = 3, 1, -3, 4


def matmultest(a, b):
    res_x = [(a[0][0]*b[0][0]+a[0][1]*b[1][0]), (a[1][0]*b[0][0]+a[1][1]*b[1][0])]
    res_y = [(a[0][0]*b[0][1]+a[0][1]*b[1][1]), (a[1][0]*b[0][1]+a[1][1]*b[1][1])]
    return res_x, res_y
a, b = matmultest(x,y)
print(a)
print(b)