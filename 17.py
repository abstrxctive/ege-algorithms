with open('17/17_16383.txt') as f:
    a = [int(x) for x in f]

def ends21_5(x):
    return (10000 <= abs(x) <= 99999) and (abs(x) % 100 == 21)

arr = [x for x in a if ends21_5(x)]
max_el_21_5 = max(arr)

k = 0
mx_s = -200_001

for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if (ends21_5(x) != ends21_5(y)) and (x**2 + y**2 >= max_el_21_5**2):
        k += 1
        mx_s = max(mx_s, x + y)

print(k, mx_s)
print(max_el_21_5)
