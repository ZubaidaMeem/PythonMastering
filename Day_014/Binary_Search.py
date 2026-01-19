def Binary_Search(List, target):
    left, right = 0, len(List) - 1
    while left <= right:
        mid = (left+right) // 2
        if List[mid] == target: return mid
        if List[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1


print(Binary_Search([1, 3, 4, 5, 5, 7, 9, 10, 11, 11], 10))
