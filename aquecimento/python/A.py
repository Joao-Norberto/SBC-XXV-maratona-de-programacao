c = int(input())
a = int(input())
v = a / (c - 1)

if v - int(v) > 0:
    v= int(v) + 1

print(int(v))