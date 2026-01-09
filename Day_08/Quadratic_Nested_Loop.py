def find_duplicates(A, B):
    matches = []
    for i in A:
        for j in B:
            if i == j:
                matches.append(i)
    return matches


A = list(range(-100,1))
B = list(range(0, 101))
matches = find_duplicates(A, B)
