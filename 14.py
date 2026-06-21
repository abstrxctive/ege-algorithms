# 1
def t7(n, b):
    res = ''
    while n > 0:
        d = n % b
        res = str(d) + res
        n = n // b
    return res

ex = 49**7 + 7**21 - 7
ex7 = t7(ex, 7)
print(ex7.count('6'))

# 2
alph = '0123456789ABCDE'
for x in alph:
    ex = int(f'123{x}5', 15) + int(f'1{x}233', 15)
    if ex % 14 == 0:
        print(ex // 14, x)

# 3
def t3(n, b):
    res = ''
    while n > 0:
        d = n % b
        res = str(d) + res
        n = n // b
    return res

for x in range(1, 2031):
    ex = 3**100 - x
    ex3 = t3(ex, 3)
    if ex3.count('0') == 5:
        print(x) 
