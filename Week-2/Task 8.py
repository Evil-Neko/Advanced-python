S1 = list(input('Enter first string: '))
S2 = list(input('Enter second string: '))
if not(len(S2) == len(S1)):
    print('NO')
else:
    for i in range(len(S2)):
        j = 0
        while j < len(S1):
            if S2[i] == S1[j]:
                S1.pop(j)
                break
            j += 1
    if not S1:
        print('YES')
    else:
        print('NO')