import math

def hypotenuse(a, b):
    return round(math.sqrt(a**2 * b**2), 2)

# First half
a1 = int(input('Enter the first side of the first triangle: '))
b1 = int(input('Enter the second side of the first triangle: '))
a2 = int(input('Enter the first side of the second triangle: '))
b2 = int(input('Enter the second side of the second triangle: '))
c1 = hypotenuse(a1, b1)
c2 = hypotenuse(a2, b2)
if c1 > c2:
    print(f'First hypotenuse = {c1}, is greater than, Second hypotenuse = {c2} ')
elif c1 < c2:
    print(f'First hypotenuse = {c1}, is smaller than, Second hypotenuse = {c2} ')
else:
    print(f'First hypotenuse = {c1}, is equal to, Second hypotenuse = {c2} ')

# Second half
text = list(input('Enter some text: ').split())
for i in range(len(text)):
    text[i] = ''.join(sorted(text[i]))
text = ' '.join(text)
print(text)