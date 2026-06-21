from functools import lru_cache

@lru_cache
def f(n):
    if n == 1:
        return 15
    else:
        return 2 * f(n - 1) - n

for i in range(1, 2025):
    f(i)
print((f(2025) - f(2023) - 2) // 2**2022)
