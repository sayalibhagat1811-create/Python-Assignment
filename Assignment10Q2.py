def Sum(no):
    ans = 0
    for i in range(1, no + 1):
        ans = ans + i
    return ans

num = int(input("Enter number: "))
print("Sum =", Sum(num))