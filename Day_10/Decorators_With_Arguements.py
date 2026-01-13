def repeat(times):
    def Decorator(new):
        def wrapper():
            for _ in range(times):new()
        return wrapper
    return Decorator

@repeat(3)
def text():
    print("Hello")

text()