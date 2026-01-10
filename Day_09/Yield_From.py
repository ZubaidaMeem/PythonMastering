sub = (x for x in range(100))
sub1 = (x for x in range(100,200))

def gen():
    yield from sub
    yield from sub1

Generator = gen()