nums = [1, 2, 3, 4, 5, 6, 7,8]
target = 15
seen = {}
for n in nums:
    if target - n in seen: print(n, target - n)
    seen[n] = 1