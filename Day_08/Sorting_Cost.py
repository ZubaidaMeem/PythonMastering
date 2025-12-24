def merge_sort(List):
    if len(List) <= 1: return List
    mid = len(List)//2
    left = merge_sort(List[0:mid])
    right = merge_sort(List[mid:])
    return merge(left,right)

def merge(left,right):
  result=[]
  i=j=0
  while i<len(left) and j<len(right):
    if left[i]<=right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1
  result.extend(left[i:])
  result.extend(right[j:])
  return result
print(merge_sort([3,1,4,2]))