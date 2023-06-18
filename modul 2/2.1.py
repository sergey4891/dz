v = float(input())
t = float(input())
x = float(input())
if v == t == x:
    print(3)
elif v == t or t == x or v == x:
    print(2)
else:
    print(0)