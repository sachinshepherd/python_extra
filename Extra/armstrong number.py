def armstrong_number(n):
    temp = n
    sum = 0
    while temp != 0:
        rem = temp % 10
        sum = sum + (rem*rem*rem)
        temp = temp / 10
    return n == sum

n = int(input("Enter number = "))
ans = armstrong_number(n)
print(ans)