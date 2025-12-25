def gcd(n, m):
    while not(n == 0):
        temp = n
        n = m % n
        m = temp
    return m

n1 = int(input('Enter first numerator: '))
m1 = int(input('Enter first denumerator: '))
n2 = int(input('Enter second numerator: '))
m2 = int(input('Enter second denumerator: '))
c1 = n1 * m2
c2 = m1 * n2
g = gcd(c1, c2)
print(f'Here is the irreducible fraction: {c1/g}/{c2/g}')