import math

def area_rectangle(a, b):
    return a * b

# First half
a = int(input('Enter the side of the hexagon: '))
print('Area =', round(((3*math.sqrt(3))/4)*(a**2), 2))

# Second half
a1 = int(input('Enter the width of first rectangle: ')) 
b1 = int(input('Enter the height of first rectangle: '))
a2 = int(input('Enter the width of second rectangle: ')) 
b2 = int(input('Enter the height of second rectangle: '))
a3 = int(input('Enter the width of third rectangle: ')) 
b3 = int(input('Enter the height of third rectangle: '))

ar1 = area_rectangle(a1, b1)
ar2 = area_rectangle(a2, b3)
ar3 = area_rectangle(a3, b2)
print('Area of the first =', ar1)
print('Area of the second =', ar2)
print('Area of the third =', ar3)
print('Total area =', ar1 + ar2 + ar3)