seq = input("Enter the string: ")
k = 0
for i in range(len(seq)-4):
    arr = seq[i] + seq[i+1] + seq[i+2] + seq[i+3] + seq[i+4]
    if arr == '>>-->' or arr == '<--<<':
        k += 1
print(k)