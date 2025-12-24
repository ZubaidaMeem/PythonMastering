def merge_sort(List):
    if len(List) <= 1: return List
    mid = len(List)//2
    left = merge_sort(List[0:mid])
    right = merge_sort(List[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

List = ["banana", "pineapple", "mango", "orange", "apple"]
List = merge_sort(List)
