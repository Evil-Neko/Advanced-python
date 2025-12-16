tix = int(input("Enter a 6 digit number: "))
left = tix // 1000
right = tix % 1000
l_sum = left//100 + (left//10)%10 + left%10
r_sum = right//100 + (right//10)%10 + right%10
if (l_sum == r_sum):
    print("YES")
else:
    print("NO")