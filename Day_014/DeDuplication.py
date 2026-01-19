List = [5, 4, 1, 3,  2, 2, 3, 5, 8, 7, 9, 6, 5]
seen = set()
result = []
for i in List:
    if i not in seen:
        seen.add(i)
        result.append(i)
print(result)
