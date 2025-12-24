def contains(List, target):
    index = 0
    length = len(List)
    while index < length:
        current_value = List[index]
        if current_value == target:
            return True
        index = index + 1
    return False

List = list(range(-1000,1000))
print(contains(List, -5))

