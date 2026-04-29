total = 0

print("Numbers from 1 to 30:")
for i in range(1, 31):
    print(i,end=" ")

print("\nGreater than 15:")
for i in range(1, 31):
    if i > 15:
        print(i,end=" ")
        total += i
print("\nSum =", total)