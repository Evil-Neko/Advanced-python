valid = 'ABCEHKMNOPTXY'
n = int(input('Enter how many license plates: '))
pl = []
i = 1
while i <= n:
    pl.append(input(f'License plate {i}: '))
    i += 1
for j in pl:
    if not(j[0] in valid) or not(j[4] in valid) or not(j[5] in valid):
        print('No')
    elif not(j[1].isdigit()) or not(j[2].isdigit()) or not(j[3].isdigit()):
        print('No')
    else:
        print('Yes')