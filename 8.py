from itertools import product

s = "АЕЛПРЬ"
nms = 0

for x in product(s, repeat=6):
    w = ''.join(x)
    
    nms += 1
    
    if nms % 2 != 0 and w[0] not in 'АЛ' and w.count('П') >= 2:
        print(nms)
        break
