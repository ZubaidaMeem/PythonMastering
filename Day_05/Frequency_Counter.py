s = input("Enter a string (ex : banana): ")

frequency = {}
for c in s:
    if c in frequency:
        frequency[c] += 1
    else :
        frequency[c] = 1

for k, v in frequency.items():
    print(k, ":" ,v)