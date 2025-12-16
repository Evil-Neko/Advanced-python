word = input("Enter a word: ")
n = int(input("Enter a number: "))
for i in word:
    k = 0
    while k < n:
        print(i, end="")
        k += 1
    print()