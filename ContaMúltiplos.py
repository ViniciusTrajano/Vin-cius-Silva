n1 = int(input())
n2 = int(input())
cont = 0
for n3 in range (1,50):
    if (n3 < 50) and (n3 % n1 == 0) and (n3 % n2 == 0):
        cont = cont + 1
print (cont)
