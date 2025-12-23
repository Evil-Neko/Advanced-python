a = input("Enter the string: ")
b = input("Enter the shifting one: ")
k = 0
for i in range(len(b)):
    loc = b[i:] + b[:i]
    step = len(b)
    for j in range(len(a) - (len(b) - 1)):
        if a[j:step] == loc:
            k +=1
        step += 1
print(k)