n=int(input('enter a limit'))
i = 1 #i=1,2

while i <= n:
    j = 1 #j=1 to 10
    while j <= 10:
        print(i, "x", j, "=", i * j)
        j = j + 1
    print()   # space between tables
    i = i + 1