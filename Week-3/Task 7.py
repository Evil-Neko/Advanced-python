import math

# First half
x = int(input('AB = '))
y = int(input('BC = '))
z = int(input('CD = '))
t = int(input('DA = '))

ac = math.sqrt(x**2+y**2)
a1 = (x*y)/2
s = (ac+z+t)/2
a2 = math.sqrt(s*(s-ac)*(s-z)*(s-t))
print('Area of the convex quadrilateral =', a1+a2)

# Second half
n = int(input('Enter a number: '))
if n <= 8:
    ans = f'000000000{n}'
    print(ans)
else:
    ans = ''
    i = n
    while not(i < 8):
        l = i%8
        i = i//8
        ans += str(l)
    ans += str(i)
    while len(ans) < 10:
        ans += '0'
    print(ans[::-1])