# на маски (маловероятно на егэ)
from fnmatch import fnmatch

res=[]
for n in range(0, 10 ** 7 + 1, 159):
    if fnmatch(str(n), '2*1?67'):
        res.append((n, n // 159))

for x, y in sorted(res):
    print(x, y)

# на делители (средняя вероятность)
def getDivisors(n):
    lst = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            lst.append(i)
    return lst

k = 0
for n in range(800_001, 100_000_000_000):
    divisors = getDivisors(n)
    M = 0
    if len(divisors) > 0:
        M = divisors[0] + divisors[-1]
    if M % 10 == 4:
        k += 1
        print(n , M)
    if k == 5:
        break

# на простые делители (высокая вероятность)
def getTrivialDivisors(n):
   answer = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           answer.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       answer.append(n)
   return answer

k = 0
for n in range(1_324_728, 1_000_000_000):
    trivial_divisors = getTrivialDivisors(n)
    if len(trivial_divisors) == 2:
        if str(trivial_divisors[0]).count('5') == 1 \
            and str(trivial_divisors[-1]).count('5') == 1:
            k += 1
            num = trivial_divisors[0] * trivial_divisors[-1]
            print(num, max(trivial_divisors))
    if k == 5:
        break
