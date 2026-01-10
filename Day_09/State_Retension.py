def running_average():
    total = 0
    n = 0
    average = None
    while True:
        value = yield average
        total += value
        n += 1
        average = total / n

ra = running_average()
next(ra)
print(ra.send(3))
print(ra.send(7))


