# на 1 кучу камней
def f(s, m):
    if s <= 16:
        return m % 2 == 0
    if m == 0:
        return False
    
    moves = [f(s-3,m-1), f(s-8,m-1), f(s//3,m-1)]
    return any(moves) if m % 2 != 0 else all(moves)

print('19)', [s for s in range(17, 150) if f(s, 2)])
print('20)', [s for s in range(17, 150) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(17, 150) if not f(s, 2) and f(s, 4)])

# на 2 кучи камней (1)
def f(s, m):
    if s >= 51:
        return m % 2 == 0
    if m == 0:
        return False
    
    moves = [f(s+1,m-1), f(s+4,m-1), f(s*2,m-1)]
    return any(moves) if m % 2 != 0 else all(moves)

task_19 = [s for s in range(1, 51) if f(s, 2)]
task_20 = [s for s in range(1, 51) if not f(s, 1) and f(s, 3)]
task_21 = [s for s in range(1, 51) if not f(s, 2) and f(s, 4)]

print('19)', task_19)
print('20)', task_20)
print('21)', task_21)

# на 2 кучи камней (2)
def f(a, b, m):
    if a + b >= 175:
        return m % 2 == 0
    if m == 0:
        return False
    
    moves = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*3, b, m-1), f(a, b*3, m-1)]
    #return any(moves) # 19
    return any(moves) if m % 2 != 0 else all(moves)

#print('19)', [s for s in range(1, 155) if f(19, s, 2)])
print('20)', [s for s in range(1, 155) if not f(19, s, 1) and f(19, s, 3)])
print('21)', [s for s in range(1, 155) if not f(19, s, 2) and f(19, s, 4)])
