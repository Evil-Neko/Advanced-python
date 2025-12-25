# First half
n = int(input('Enter a number: '))
i = 0
while i < n:
    i += 1
    if i < 10:
        print(i, end=' ')
    elif '0' in str(i):
        continue
    else:
        k = 0
        for j in str(i):
            if i%int(j)==0:
                k += 1
        if k == len(str(i)):
            print(i, end=' ')
print()

# Second half
m = int(input('Enter the length of the array: '))
arr = []
i = 0
print('Enter the elements of the array: ')
while i < m:
    el = int(input())
    arr.append(el)
    i += 1
new_arr = []
for j in arr[::-1]:
    new_arr.append(j)
print(f'Original array: {arr}; New array: {new_arr}')