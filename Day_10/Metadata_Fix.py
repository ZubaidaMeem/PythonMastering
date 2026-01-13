def deco(new):
    def wrapper(): pass
    return wrapper

@deco
def test(): pass

print(test.__name__)