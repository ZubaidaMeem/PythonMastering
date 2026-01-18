import time

class Timer:
    def __enter__(self): self.t = time.time()
    def __exit__(self, *_): print(time.time() - self.t)

with Timer():
    time.sleep(1)
