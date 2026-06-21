from math import log2, ceil

# обычный прототип
d = 32
n = 250
i = ceil(log2(n))
num = ceil((d*i) / 8)

print(3200*num / 1024)

# поиск мощности алфавита
from math import *

for m in range(1, 10**5):
    d = 257
    i = ceil(log2(m))
    num = ceil((d*i)/8)
    if 295_740*num <= 33*1024*1024:
        print(m)

# поиск длины серийного номера
from math import *

m = 10 + 17
i = ceil(log2(m))
for d in range(1, 10**5):
    n = ceil((d*i)/8)
    if 7_564_230*n > 31*1024*1024:
        print(d)
        break
