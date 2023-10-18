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

a = length
fig = plt.figure()

xc = np.array([0, 0, a, a, 0, 0, a, a])
yc = np.array([0, a, a, 0, 0, a, a, 0])
zc = np.array([0, 0, 0, 0, a, a, a, a])

cube = [[0 for j in range(3)] for i in range(8)]
for i in range(0,8):
    cube[i] = [xc[i], yc[i], zc[i]]

def move_cube(cube, coeff):
    mCube = [[0 for j in range(3)] for i in range(8)]
    for i in range(0,8):
        mCube[i][0] = cube[i][0] + coeff
        mCube[i][1] = cube[i][1] + coeff
        mCube[i][2] = cube[i][2] + coeff
    return mCube

def scale_cube(cube, coeff):
    sCube = [[0 for j in range(3)] for i in range(8)]
    for i in range(0,8):
        sCube[i][0] = cube[i][0] * coeff
        sCube[i][1] = cube[i][1] * coeff
        sCube[i][2] = cube[i][2] * coeff
    return sCube

def rotate_cube_Z(cube, angle):
    rZCube = [[0 for j in range(3)] for i in range(8)]
    for i in range(0, 8):
        rZCube[i][0] = cube[i][0] * np.cos(angle) + cube[i][1] * np.sin(angle)
        rZCube[i][1] = cube[i][1] * np.cos(angle) - cube[i][0] * np.sin(angle)
        rZCube[i][2] = cube[i][2]
    return rZCube

def rotate_cube_Y(cube, angle):
    rYCube = [[0 for j in range(3)] for i in range(8)]
    for i in range(0, 8):
        rYCube[i][0] = cube[i][0] * np.cos(angle) - cube[i][2] * np.sin(angle)
        rYCube[i][1] = cube[i][1]
        rYCube[i][2] = cube[i][0] * np.sin(angle) + cube[i][2] * np.cos(angle)
    return rYCube

def rotate_cube_X(cube, angle):
    rXCube = [[0 for j in range(3)] for i in range(8)]
    for i in range(0, 8):
        rXCube[i][0] = cube[i][0]
        rXCube[i][1] = cube[i][1] * np.cos(angle) + cube[i][2] * np.sin(angle)
        rXCube[i][2] = cube[i][2] * np.cos(angle) - cube[i][1] * np.sin(angle)
    return rXCube

axes = fig.add_subplot(projection='3d')

axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_zlabel('Z')

def draw_cube(cube, color):
    for i in range(0,4):
        for j in range(0, 2):
            plt.plot([cube[i + j * 4][0], cube[(i + 1)%4 + j * 4][0]], [cube[i + j * 4][1], cube[(i + 1)%4 + j * 4][1]], [cube[j * 4 + i][2], cube[j * 4 + (i+1)%4][2]], color)
        plt.plot([cube[i][0], cube[i+4][0]], [cube[i][1], cube[i+4][1]], [cube[i][2], cube[i+4][2]], color)

draw_cube(cube, 'k')
draw_cube(move_cube(cube, move_coeff), 'y')
draw_cube(scale_cube(cube, scale_coeff), 'purple')
draw_cube(rotate_cube_Z(cube, angle), 'b')
draw_cube(rotate_cube_Y(cube, angle), 'g')
draw_cube(rotate_cube_X(cube, angle), 'r')

plt.show()
