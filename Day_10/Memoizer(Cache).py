def cache(new):
    Dict = {}
    def wrapper(n):
        if n in Dict: return Dict[n]
        Dict[n] = new(n)
        return Dict[n]
    return wrapper

@cache
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n -2)

print(fibonacci(3))

