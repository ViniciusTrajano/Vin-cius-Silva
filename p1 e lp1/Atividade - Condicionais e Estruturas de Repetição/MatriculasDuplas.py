p2=[]
p3=[]
i=0
for i in range (45):
    n=int(input())
    p2.append(n)
    i=i+1
#print ("Lista 1:",p2)
for i in range (30):
    n=int(input())
    p3.append(n)
    i=i+1
#print ("lista 2:",p3)
inter=[]
for num in p2:
  if num in p3:
      inter.append(num)
print(inter)

#Não recebe entradas seguidas de Espaçamentos como a questão pede.
