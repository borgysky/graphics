import matplotlib.pyplot as plt
import numpy as np

x1, y1, x2, y2 = input("Координаты 1го отрезка:").split(',')
a1, b1, a2, b2 = input("Координаты 2го отрезка:").split(',')
c1, d1, c2, d2 = input("Координаты 3го отрезка:").split(',')
length = int(input("Длина стороны куба:"))
move_coeff = int(input("Коэффициент перемещения:"))
scale_coeff = int(input("Коэффициент масштабирования:"))
angle = float(input("Угол поворота:"))
x1, y1, x2, y2, a1, b1, a2, b2, c1, d1, c2, d2 = int(x1), int(y1), int(x2), int(y2), int(a1), int(b1), int(a2), int(b2), int(c1), int(d1), int(c2), int(b2)

def move_segment(x1, y1, x2, y2, coeff):
    res_x = [x1 + coeff, x2 + coeff]
    res_y = [y1 + coeff, y2 + coeff] 
    return res_x, res_y

def scale_segment(x1, y1, x2, y2, coeff):
    coords = [[0 for x in range(2)] for y in range(2)]
    coords[0][0], coords[0][1], coords[1][0], coords[1][1] = x1, y1, x2, y2
    mul_coeff = [[0 for x in range(2)] for y in range(2)]
    mul_coeff[0][0], mul_coeff[0][1], mul_coeff[1][0], mul_coeff[1][1] = coeff, 0, 0, coeff
    return matmul(coords, mul_coeff)

def rotate(x1, y1, x2, y2, angle):
    coords = [[0 for x in range(2)] for y in range(2)]
    coords[0][0], coords[0][1], coords[1][0], coords[1][1] = x1, y1, x2, y2
    rotate_coeff = [[0 for x in range(2)] for y in range(2)]
    rotate_coeff[0][0], rotate_coeff[0][1], rotate_coeff[1][0], rotate_coeff[1][1] = np.cos(angle), np.sin(angle), np.sin(angle) * -1, np.cos(angle)
    return matmul(coords, rotate_coeff)

def matmul(a, b):
    res_x = [(a[0][0]*b[0][0]+a[0][1]*b[1][0]), (a[1][0]*b[0][0]+a[1][1]*b[1][0])]
    res_y = [(a[0][0]*b[0][1]+a[0][1]*b[1][1]), (a[1][0]*b[0][1]+a[1][1]*b[1][1])]
    return res_x, res_y

plt.plot([x1, x2], [y1, y2], color = 'r')
plt.plot([a1, a2], [b1, b2], color = 'g')
plt.plot([c1, c2], [d1, d2], color = 'b')
x, y = move_segment(x1,y1,x2,y2,move_coeff)
a, b = move_segment(a1,b1,a2,b2,move_coeff)
c, d = move_segment(c1,d1,c2,d2,move_coeff) 
plt.plot(x,y, color = 'r')
plt.plot(a,b, color = 'g')
plt.plot(c,d, color = 'b')
x, y = scale_segment(x1,y1,x2,y2,scale_coeff)
a, b = scale_segment(a1,b1,a2,b2,scale_coeff)
c, d = scale_segment(c1,d1,c2,d2,scale_coeff)
plt.plot(x,y, color = 'r')
plt.plot(a,b, color = 'g')
plt.plot(c,d, color = 'b')
x, y = rotate(x1,y1,x2,y2,angle)
a, b = rotate(a1,b1,a2,b2,angle)
c, d = rotate(c1,d1,c2,d2,angle)
plt.plot(x,y, color = 'r')
plt.plot(a,b, color = 'g')
plt.plot(c,d, color = 'b')
plt.show()