s = ""
def add_char(old_string, char):
    old_size = len(old_string)
    new_size = old_size + 1
    new_memory = [''] * new_size
    for i in range(old_size):
        new_memory[i] = old_string[i]
    new_memory[old_size] = char
    return "".join(new_memory)

for i in range(10000):
    s = add_char(s,'a')