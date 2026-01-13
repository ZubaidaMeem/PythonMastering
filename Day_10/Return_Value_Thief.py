def Decorator(new):
    def wrapper(*args):
        print("Args:", args)
        new(*args)
    return wrapper

@Decorator
def add(a,b):
    return a + b

add(1,2)