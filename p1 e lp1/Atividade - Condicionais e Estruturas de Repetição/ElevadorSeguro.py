pesos = []
pt = 0
ptt = 0
while True:
    p = input()
    pt = float(p) + pt
    if (float(p) != 0) and (pt <= 560):
        pesos.append(p)
        ptt = ptt + float(p)
    else:
        break

print (len(pesos))
print (ptt)
