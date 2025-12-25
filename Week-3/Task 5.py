def gcd(n, m):
    while not(n == 0):
        temp = n
        n = m % n
        m = temp
    return m

# First half
n1 = int(input('Enter first numerator: '))
m1 = int(input('Enter first denumerator: '))
n2 = int(input('Enter second numerator: '))
m2 = int(input('Enter second denumerator: '))
if m1 == m2:
    c1 = n1 - n2
    c2 = m1
    g = gcd(c1, c2)
    print(f'Here is the irreducible fraction: {c1/g}/{c2/g}')
elif m1%m2==0:
    c1 = n1 - (n2*(m1/m2))
    c2 = m1
    g = gcd(c1, c2)
    print(f'Here is the irreducible fraction: {c1/g}/{c2/g}')
elif m2%m1==0:
    c1 = (n1*(m2/m1)) - n2
    c2 = m2
    g = gcd(c1, c2)
    print(f'Here is the irreducible fraction: {c1/g}/{c2/g}')
else:
    c1 = (n1*m2) - (n2*m1)
    c2 = m1*m2
    if c1 < 0:
        g = gcd(-c1, c2)
    else:
        g = gcd(c1, c2)
    print(f'Here is the irreducible fraction: {c1/g}/{c2/g}')

# Seconf half
num = int(input('Enter a number: '))
i = 1
while i <= num:
    if num%i==0:
        print(i, end=' ')
    i += 1