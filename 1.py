from itertools import permutations

s = '24 146 56 1267 36 23457 46'.split()
v = 'АБ АВ БВ ВД ВГ ВЕ ДЕ ГЕ ГК ЕК '.split()
print(*range(1, 8))
for p in permutations('АБВГДЕК'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a, b in v):
        print(*p)
