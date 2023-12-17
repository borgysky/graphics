import matplotlib.pyplot as plt
import numpy as np

surfaces = []
ymax = np.full(101, 0.)
ymin = []

b0 = np.array([0, 2])
b1 = np.array([5, 3])
b2 = np.array([9, 3])
b3 = np.array([10, 2])

c0 = np.array([0, 1])
c1 = np.array([3, 2])
c2 = np.array([4, 2])
c3 = np.array([10, 1])

d0 = np.array([0, 1.33])
d1 = np.array([4, 2.5])
d2 = np.array([6, 2.5])
d3 = np.array([10, 1.33])

e0 = np.array([0, 1.67])
e1 = np.array([7, 3.5])
e2 = np.array([8, 3.5])
e3 = np.array([10, 1.67])

a0 = np.array([0, 1.5])
a1 = np.array([5, 4])
a2 = np.array([6, 4])
a3 = np.array([10, 1.5])

n = np.arange(0, 1.01, 0.01)

def drawfunc(P0, P1, P2, P3):
    a = []
    b = []
    for index, x in enumerate(n):
        y = func1(x, P0, P1, P2, P3)
        a.append(x)
        b.append(y)
    return (a, b)

def func1(x, P0, P1, P2, P3):
    y = (1 - x) ** 3 * P0[1] + 3 * (1 - x) ** 2 * x * P1[1] + 3 * (1 - x) * x ** 2 * P2[1] + x ** 3 * P3[1]
    return y

def floatinghorizon(P0, P1, P2, P3):
    global ymax
    a = []
    b = []
    for index, x in enumerate(n):
        y = func1(x, P0, P1, P2, P3)
        if y > ymax[index]:
            ymax[index] = y
        else:
            y = ymax[index]
        a.append(x)
        b.append(y)
    return (a, b)


z, w = floatinghorizon(c0, c1, c2, c3)
k, h = floatinghorizon(d0, d1, d2, d3)
a, b = floatinghorizon(a0, a1, a2, a3)
e, r = floatinghorizon(e0, e1, e2, e3)
c, d = floatinghorizon(b0, b1, b2, b3)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
ax1.set_title('До обработки:')
ax2.set_title('После (плавающий горизонт):')
ax3.set_title('До обработки:')
ax4.set_title('После (Z-буфер):')

ax2.plot(a, b, color = 'black')
ax2.plot(c, d, color = 'black')
ax2.plot(z, w, color = 'black')
ax2.plot(k, h, color = 'black')
ax2.plot(e, r, color = 'black')

z, w = drawfunc(c0, c1, c2, c3)
k, h = drawfunc(d0, d1, d2, d3)
a, b = drawfunc(a0, a1, a2, a3)
e, r = drawfunc(e0, e1, e2, e3)
c, d = drawfunc(b0, b1, b2, b3)

ax1.plot(a, b, color = 'black')
ax1.plot(c, d, color = 'black')
ax1.plot(z, w, color = 'black')
ax1.plot(k, h, color = 'black')
ax1.plot(e, r, color = 'black')

y = np.array([[50, 50, 0], [100, 100, -100], [50, 150, 0], [100, 200, -100],
              [150, 50, 0], [150, 150, 0]])

x = np.array([[1, 2], [2, 4], [4, 3], [3, 1]])
w = np.array([[1, 3], [3, 6], [6, 5], [5, 1]])

z_buffer = np.full((300, 500), -100.)
frame_buffer = np.full((300, 500, 3), 255)
res = np.full((300, 500, 3), 255)

def zbuffer(p1, p2, i, j, color):
    if p1[0] == p2[0] and p1[1] == p2[1]:
        frame_buffer[p1[0], p1[1]] = [254, 0, 0]
        return

    if abs(p2[0] - p1[0]) >= abs(p2[1] - p1[1]):
        L = abs(p2[0] - p1[0])
    else:
        L = abs(p2[1] - p1[1])

    dx = (p2[0] - p1[0]) / L
    dy = (p2[1] - p1[1]) / L

    cur_x = p1[0] + 0.5 * np.sign(dx) + i
    cur_y = p1[1] + 0.5 * np.sign(dy) + j
    for i in range(1, L + 1):
        if i == 0:
            if p1[0] < 150:
                z = 2 * cur_x - 100
            else:
                z = 2 * cur_x - 300
        else:
            z = p1[2]
        if z > z_buffer[int(cur_x), int(cur_y)]:
            frame_buffer[int(cur_x), int(cur_y)] = color
            z_buffer[int(cur_x), int(cur_y)] = -z
        cur_x = cur_x + dx
        cur_y = cur_y + dy

def draw(p1, p2, i, j, color):
    if p1[0] == p2[0] and p1[1] == p2[1]:
        frame_buffer[p1[0], p1[1]] = [254, 0, 0]
        return

    if abs(p2[0] - p1[0]) >= abs(p2[1] - p1[1]):
        L = abs(p2[0] - p1[0])
    else:
        L = abs(p2[1] - p1[1])

    dx = (p2[0] - p1[0]) / L
    dy = (p2[1] - p1[1]) / L

    cur_x = p1[0] + 0.5 * np.sign(dx) + i
    cur_y = p1[1] + 0.5 * np.sign(dy) + j
    for i in range(1, L + 1):
        res[int(cur_x), int(cur_y)] = color
        cur_x = cur_x + dx
        cur_y = cur_y + dy


for i in range(100):
    zbuffer(y[w[0][0] - 1], y[w[0][1] - 1], i, 0, [255, 255, 0])
    draw(y[w[0][0] - 1], y[w[0][1] - 1], i, 0, [255, 255, 0])

for i in range(100):
    zbuffer(y[x[0][0] - 1], y[x[0][1] - 1], 0, i, [255, 0, 0])
    draw(y[x[0][0] - 1], y[x[0][1] - 1], 0, i, [255, 0, 0])

ax3.imshow(res)
ax4.imshow(frame_buffer)

plt.show()
