def pop_from_start(List):
    target = List[0]
    N = len(List)
    for i in range(0, N - 1):
        List[i] = List[i + 1]
    List.pop()
    return List

List = list(range(10))
print(List)
List = pop_from_start(List)
print(List)
List.pop()
print(List)