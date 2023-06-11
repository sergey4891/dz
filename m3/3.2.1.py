nums = [1, 4, 1, 6, "hello", 'a', 5,"hello"]

dup = [x for i, x in enumerate(nums) if x in nums[:i]]
print(dup)
