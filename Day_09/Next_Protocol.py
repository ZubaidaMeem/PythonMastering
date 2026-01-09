Generator = (x for x in range(100))
# while True:
#     print(next(Generator))
while True:
    try:
        print(next(Generator))
    except StopIteration:
        break
