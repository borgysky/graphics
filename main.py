import matplotlib
import numpy as np

x1, y1, x2, y2 = input("Координаты 1го отрезка:").split(',')
a1, b1, a2, b2 = input("Координаты 2го отрезка:").split(',')
c1, d1, c2, d2 = input("Координаты 3го отрезка:").split(',')
length = input("Длина стороны куба:")
move_coeff = input("Коэффициент перемещения:")
scale_coeff = input("Коэффициент масштабирования:")

def move_segment(x1, y1, x2, y2, coeff):
    x1_res = x1 + coeff
    y1_res = y1 + coeff
    x2_res = x2 + coeff
    y2_res = y2 + coeff
    return x1_res, y1_res, x2_res, y2_res


def scale_segment(x1, y1, x2, y2, coeff):
    coords = [[0 for x in range(2)] for y in range(2)]
    coords[0][0], coords[0][1], coords[1][0], coords[1][1] = x1, y1, x2, y2
    mul_coeff = [[0 for x in range(2)] for y in range(2)]
    mul_coeff[0][0], mul_coeff[0][1], mul_coeff[1][0], mul_coeff[1][1] = coeff, 0, 0, coeff
    res = np.matmul(coords, mul_coeff)
    return res

