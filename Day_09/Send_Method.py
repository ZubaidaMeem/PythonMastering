def coroutine():
    i = 0
    while True:
        value = yield i
        if value: i += value
        else: i += 1
        print(i)

x = coroutine()
next(x)
for _ in range(100): x.send(3)


