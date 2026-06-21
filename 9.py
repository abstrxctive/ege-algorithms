k = 0
with open('9') as f:
    for s in f:
        a = [int(x) for x in s.split()]
        povt = [int(x) for x in a if a.count(x) == 3]
        nepovt = [int(x) for x in a if a.count(x) == 1]
        if len(povt) == 6 and len(nepovt) == 1 and max(povt) > nepovt[0]:
            k += 1
print(k)
