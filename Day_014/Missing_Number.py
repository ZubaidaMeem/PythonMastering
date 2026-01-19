nums = list(range(1, 101))
nums.remove(99)
n = 100
print(n * (n + 1) // 2 - sum(nums))
