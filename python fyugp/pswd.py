import random

letters = "abcdefghijklmnopqrstuvwxyz"

for i in range(100):
    word = ""
    for j in range(5):
        word += random.choice(letters)
    print(word)