def s_tr(a, b, c):
    p = (a+b+c)/2
    return pow(p * (p-a) * (p-b) * (p-c), 0.5)

print (s_tr(2,2,2))
