import random
with open("camelot.txt","r") as f:
    print(f.read(2))
    print(f.read(8))
    print(f.read(7))
    print(f.read())

for i in range(3):
    print((random.uniform(0,100)))