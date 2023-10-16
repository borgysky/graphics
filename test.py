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