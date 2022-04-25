num = int(input("Please in put a positive integer. "))
fac = 1
while num > 0:
    fac *= num
    num -= 1

print(str(fac))