import matplotlib.pyplot as plt
inside = 0 
left = 1 
right = 2 
bottom = 4 
top = 8 
x_max, x_min = input("x_max, x_min:").split(',')
y_max, y_min = input("y_max, y_min:").split(',')
x_max, x_min, y_max, y_min = int(x_max), int(x_min), int(y_max), int(y_min)
x1, y1, x2, y2 = input("Координаты 1го отрезка:").split(',')
a1, b1, a2, b2 = input("Координаты 2го отрезка:").split(',')
c1, d1, c2, d2 = input("Координаты 3го отрезка:").split(',')
x1, y1, x2, y2, a1, b1, a2, b2, c1, d1, c2, d2 = int(x1), int(y1), int(x2), int(y2), int(a1), int(b1), int(a2), int(b2), int(c1), int(d1), int(c2), int(b2)

def computeCode(x, y):
	tag = inside
	if x < x_min: 
		tag |= left
	elif x > x_max: 
		tag |= right
	if y < y_min: 
		tag |= bottom
	elif y > y_max: 
		tag |= top
	return tag

def clip(x1, y1, x2, y2):
	tag1 = computeCode(x1, y1)
	tag2 = computeCode(x2, y2)
	accept = False
	while True:
		if tag1 == 0 and tag2 == 0:
			accept = True
			break
		elif (tag1 & tag2) != 0:
			break
		else:
			x = 1.0
			y = 1.0
			if tag1 != 0:
				code_out = tag1
			else:
				code_out = tag2
			if code_out & top:
				x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
				y = y_max
			elif code_out & bottom:
				x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
				y = y_min
			elif code_out & right:
				y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
				x = x_max
			elif code_out & left:
				y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
				x = x_min
			if code_out == tag1:
				x1 = x
				y1 = y
				tag1 = computeCode(x1, y1)
			else:
				x2 = x
				y2 = y
				tag2 = computeCode(x2, y2)
	if accept:
		plt.plot([x1, x2], [y1,y2])

plt.plot([x_min, x_min], [y_min, y_max], color = 'r')
plt.plot([x_max, x_max], [y_min, y_max], color = 'r')
plt.plot([x_min, x_max], [y_min, y_min], color = 'r')
plt.plot([x_min, x_max], [y_max, y_max], color = 'r')
clip(x1, y1, x2, y2)
clip(a1, b1, a2, b2)
clip(c1, d1, c2, d2)
plt.show()