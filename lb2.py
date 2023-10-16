import matplotlib.pyplot as plt
import numpy as np

xc, yc = input("Введите координаты (x,y) центра:").split(',')
R = input("Радиус окружности:")
xc, yc, R = int(xc), int(yc), int(R)
x, y, delta, yk = 0, R, 2 * (1-R), 0
res = np.full((max((xc+R)*2,200),max((yc+R)*2,200),3),255)
def circle(xc,yc,R):
    x = 0
    y = R
    delta = 1 - 2 * R
    error = 0
    while y >=x:
        res[xc + x, yc + y] = [255, 0, 0]
        res[xc + x, yc - y] = [255, 0, 0]
        res[xc - x, yc + y] = [255, 0, 0]
        res[xc - x, yc - y] = [255, 0, 0]
        res[xc + y, yc + x] = [255, 0, 0]
        res[xc + y, yc - x] = [255, 0, 0]
        res[xc - y, yc + x] = [255, 0, 0]
        res[xc - y, yc - x] = [255, 0, 0]
        error = 2 * (delta+y) - 1
        if delta < 0 and error <= 0:
            x += 1
            delta += 2 * x + 1
            continue
        error = 2 * (delta - x) - 1
        if delta > 0 and error > 0:
            y -= 1
            delta += 1 - 2 * y
            continue
        x += 1
        delta += 2 * (x-y)
        y -= 1
    return res

plt.imshow(circle(xc,yc,R))
plt.show()