a = list(map(int, input('Enter two numbers: ').split()))
text = input(f'Enter {a[0]} characters: ')
m = a[1]
check = []
k = 0
for i in range(len(text) - (m - 1)):
    w = text[i:m]
    if not(w in check):
        check.append(w)
        k += 1
    m += 1
print(k)