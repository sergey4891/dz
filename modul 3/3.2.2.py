my_digits =  [[12, 3, 8, 4, 15, 13, 10, 2, 9, 11],
[12, 3, 8, 4, 15, 13, 10, 2, 9, 11],
[12, 3, 8, 4, 15, 13, 10, 2, 9, 50],
[12, 3, 8, 4, 15, 13, 10, 2, 9, 11]]
max = 0
for i in my_digits:
    for j in i:
        if j > max:
            max = j
print(max)
