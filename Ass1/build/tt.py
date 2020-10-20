import random as rd

b = rd.sample(range(0, 11), 10)

for value in b:
    print(b[value], ":", value)

print(b)
