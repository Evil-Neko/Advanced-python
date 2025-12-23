pur = list(input('Enter the purchased items: ').split())
new_l = {}
for i in range(len(pur)):
    w = pur[i]
    k = 0
    if w not in new_l:
        for j in range(len(pur)):
            if pur[i] == pur[j]:
                k += 1
        new_l[pur[i]] = k
print('Purchase frequency:')
for prod, freq in new_l.items():
    print(f"{prod}: {freq}")
m = new_l[max(new_l, key=new_l.get)]
print('Most popular items:', end=' ')
for prod, freq in new_l.items():
    if freq == m:
        print(prod, end=' ')
print()
print('Purchased once:', end=' ')
for prod, freq in new_l.items():
    if freq == 1:
        print(prod, end=' ')
print()
new_l = dict(sorted(new_l.items(), key=lambda item: item[1], reverse=True))
for prod, freq in new_l.items():
    print(f"{prod} {freq}")