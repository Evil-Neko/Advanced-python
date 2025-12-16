a = float(input("Enter a number: "))
a_int = int(a)
a_frac = a - a_int
new_a = a_frac * 100 + a_int / 100
print(round(new_a, 2))