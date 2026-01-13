import time
def timer(new):
    def wrap():
        start = time.time()
        new()
        print(time.time()-start)
    return wrap

@timer
def work(): time.sleep(.5)

work()