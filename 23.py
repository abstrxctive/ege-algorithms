# 1 самый обычный прототип
def f(x, y):
    if x > y or x == 60:
        return 0
    elif x == y:
        return 1
    return f(x+5, y) + f(x*5, y)

print(f(5, 30) * f(30, 280))

# на поменяй местами (новый прототип, высокая вероятность встретить на егэ)
def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
      if str(x)[1] < str(x)[2]:
        return f(x+1, y) + f( int( str(x)[0] + str(x)[2] + str(x)[1] ), y)
      else:
        return f(x+1, y)

print(f(100, 150))
