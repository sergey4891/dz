def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while (j >= 0 and temp < list[j]):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp


list = [2, 7, 8, 6, 0, 4, 1, 9, 3, 5]
# list = input('Введите массив: ').split()
# list = [int(x) for x in list]
insertion_sort(list)
print('Отсортированый массив: ', end='')
print(list)