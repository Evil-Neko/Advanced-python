def check_insideness(x, y, a, b, R):
    pos = (x-a)**2+(y-b)**2
    return pos < R**2

a, b = map(int, input('Enter the center positon of the circle: ').split())
r = int(input('Enter the radius of the circle: '))
p1, p2 = map(int, input('Enter the position of the first point: ').split())
f1, f2 = map(int, input('Now of the second: ').split())
l1, l2 = map(int, input('Aaaand the third: ').split())
c = 0
if check_insideness(p1, p2, a, b, r):
    c += 1
if check_insideness(f1, f2, a, b, r):
    c += 1
if check_insideness(l1, l2, a, b, r):
    c += 1
print(c)