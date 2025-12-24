def set_contains(Set, target):
    hash_value = hash(target)
    bucket_index = hash_value % len(Set)
    memory_slot = Set[bucket_index]
    if target in memory_slot: return True
    else: return False

Set = [[] for i in range(20000)]

for i in range(-10000, 10001):
    index = hash(i) % len(Set)
    Set[index].append(i)
print(set_contains(Set, -5))