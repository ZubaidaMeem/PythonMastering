def Decorator(new):
    def wrapper():
        print("Before")
        new()
        print("After")
    return wrapper

@Decorator
def middle(): print("Middle")

middle()
