List = [x for x in range(1000000)]
Generator = (x for x in range(1000000))

import sys
List_size = sys.getsizeof(List)
Generator_size = sys.getsizeof(Generator)
print(List_size, Generator_size)