n = int(input("Enter a limit: "))
x = 0

while x < n:
    x = x + 1
    if x % 2 == 0:
        continue #use of continue
    print(x)