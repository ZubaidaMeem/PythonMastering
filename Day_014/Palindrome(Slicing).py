s = 'Madam'
c = ''.join(x.lower() for x in s if x.isalnum())
print(c == c[::-1])
