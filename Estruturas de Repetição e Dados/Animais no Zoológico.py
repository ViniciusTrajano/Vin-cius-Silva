t = []
l = []
p = 0
qt = 0
qm = 0
qcv = 0
while True:
    n=input()
    if n.lower() == 'parar':
        l.append(t)
        break
    elif n.lower() == 'continuar':
        l.append(t)
        t = []
    else:
        t.append(n.lower())
for i in l:
    if 'tigre' in i:
        p += float(i[1])
        qt += 1
    elif ('cobra' and 'venezuela') in i:
        qcv += 1
    elif 'macaco' in i:
        qm += 1
pt = p/qt  
print(qm)
print('{:.2f}'.format(pt))
print(qm)
