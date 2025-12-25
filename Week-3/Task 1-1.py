import math

def area_square(a):
    return a ** 2

def area_rectangle(a, b):
    return a * b

def area_triangle(b, h):
    return 1/2 * b * h

def area_circle(r):
    return round((math.pi * (r**2)), 2)

choice = input('Which shape do you want? ').lower()
if choice == 'square':
    size = int(input('Enter the size of the squares sides: '))
    print('Area =', area_square(size))
elif choice == 'rectangle':
    width = int(input('Enter the width of the rectangle: '))
    height = int(input('Enter the height of the rectangle: '))
    print('Area =', area_rectangle(width, height))
elif choice == 'triangle':
    base = int(input('Enter the base of the triangle: '))
    height = int(input('Enter the height of the triangle: '))
    print('Area =', area_triangle(base, height))
elif choice == 'circle':
    radius = int(input('Enter the radius of the circle: '))
    print('Area =', area_circle(radius))
else:
    print("Maaan sorry, but I don't know such shapes D;")