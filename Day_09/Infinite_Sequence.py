def Fibonacci():
    i , j = 0, 1
    while True:
        yield i
        i , j = j, i + j

n = Fibonacci()
for i in range(100):
    print(next(n))
