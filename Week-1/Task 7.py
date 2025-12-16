a = int(input("First number: "))
ac = input("Operation: ")
b = int(input("Second number: "))
if (ac == "+"):
    print("Here is the result: ", a + b)
elif (ac == "-"):
    print("Here is the result: ", a - b)
elif (ac == "*"):
    print("Here is the result: ", a * b)
elif (ac == "/"):
    if (b == 0):
        print("DON'T DO THAT DUDE")
    else:
        print("Here is the result: ", a / b)
else:
    print("That ain't an operation dude")