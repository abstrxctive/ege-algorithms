# 1
for A in range(1, 1000):
    for x in range(1, 1000):
        ok = (x % A != 0) <= ((x % 6 == 0) <= (x % 9 != 0))
        if not ok:
            break
    if ok:
        print(A)
# 2 
P = list(range(17, 55)) # наим длина
Q = list(range(37, 84))
A = []
for x in range(17, 84):
    ok = (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))
    if not ok:
        A.append(x)
print(len(A)-1) # 11

# маловероятно, но могут добавить на егэ 2027 (прототип из сборника Крылова)
# Возвращает нетривиальные делители числа n
def getDivisors(n):
    lst = []
    for i in range(2, n // 2):
        if n % i == 0:
            lst.append(i)
    return lst

A = list(range(3, 61))
B = getDivisors(177)

valid_y = []

for y in range(2, 10000):
    C = getDivisors(y)
    
    if not C:
        continue
    
    for x in C:
        ok = (x in C) <= ((x in A) and (not(x in B)))
        if not ok:
            break
    
    if ok:
        valid_y.append(y)
    
print(max(valid_y))
