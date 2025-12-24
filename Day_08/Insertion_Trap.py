def insert_at_zero(List, new_val):
    N = len(List)
    List.append(None)
    for i in range(N, 0, -1):
        List[i] = List[i - 1]
    List[0] = new_val
    return List

List = [2, 3, 4, 5]
List = insert_at_zero(List, 1)
