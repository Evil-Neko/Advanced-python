import math

def gcd(n, m):
    while not(n == 0):
        temp = n
        n = m % n
        m = temp
    return m

# First half
a, b = map(int, input('Enter two numbers: ').split())
print('GCD =', gcd(a, b), 'LCM =', (a*b)/gcd(a, b))

# Second half
a = int(input('AB = '))
b = int(input('BC = '))
c = int(input('CD = '))
d = int(input('DA = '))
p = int(input('Diagonal = '))

s1 = (a+b+p)/2
tri1 = math.sqrt(s1*(s1-a)*(s1-b)*(s1-p))
s2 = (c+d+p)/2
tri2 = math.sqrt(s2*(s2-c)*(s2-d)*(s2-p))
print('Area of the convex quadrilateral =', tri1+tri2)