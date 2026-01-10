def square(n):
    for i in range(n):
        yield i * i

def filter(nums):
    for i in nums:
        if i % 2 == 0 : yield i

chain = filter(square(100))
