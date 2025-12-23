eq = input('Enter the equation: ')
if eq[1] == '+':
    if eq[0] == 'x':
        ans = int(eq[4]) - int(eq[2])
    elif eq[2] == 'x':
        ans = int(eq[4]) - int(eq[0])
    else:
        ans = int(eq[0]) + int(eq[2])
else:
    if eq[0] == 'x':
        ans = int(eq[4]) + int(eq[2])
    elif eq[2] == 'x':
        ans = -(int(eq[4]) - int(eq[0]))
    else:
        ans = int(eq[0]) - int(eq[2])
print(ans)