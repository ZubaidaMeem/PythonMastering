class PyListObject:
    def __init__(self, size):
        self.ob_size = size

def get_length(list_obj):
    return list_obj.ob_size

items = [None] * 100000000
List = PyListObject(len(items))
Length = get_length(List)
# print(Length)