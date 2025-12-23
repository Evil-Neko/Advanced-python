def all_eq(l):
    m = len(max(l))
    for i in range(len(l)):
        if len(l[i]) < m:
            while len(l[i]) < m:
                l[i] += '_'
    return l
a = list(input("Enter a bunch o' strings: ").split())
print(all_eq(a))