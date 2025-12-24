def slice_list(source,k):
    new_list=[None] * k
    for i in range(0, k):
        new_list[i] = source[i]
    return new_list
data = list(range(10000))
sub = slice_list(data,1000)
# print(sub)
# print(data)