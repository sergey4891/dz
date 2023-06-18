x = int(input('Вклад: '))
p = int(input('Процент: '))
y = int(input('Сумма: '))
count = 0
while x <= y:
    x += int(x * p / 100)
    count += 1
print(x)
print(count)
