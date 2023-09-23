def binary_search(list, item):
  low = 0
  high = len(list) - 1
  i = 0
  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
    i=i+1
  return None

my_list = [6, 17, 21, 27, 32, 35, 36, 37, 48]
print(binary_search(my_list, 35))