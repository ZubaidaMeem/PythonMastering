a = [1, 1, 3, 5, 7]
b = [2, 4, 5, 6, 8, 9]
i = j = 0
result = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1
result += a[i:] + b[j:]
print(result)
