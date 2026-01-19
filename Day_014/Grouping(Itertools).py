from itertools import groupby
data = sorted('yaaaebbdcfhg')
for k, g in groupby(data): print(k, list(g))
