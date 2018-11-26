#Criar Lista:
n = int(input())
lista = []
for i in range (0,n):
    n2 = int(input())
    lista.append(n2)
#Inverter Lista:
print(lista[::-1])

#Passar uma casa para a esquerda:
lista_inver = []
lista_ordem = sorted(lista)
maxi = max(lista)
for i in range (0,n):
    resto = (lista_ordem[i] % maxi)
    if resto != 0:
        lista_inver.append(lista[i+1])
    else:
        lista_inver.append(lista[0])
print(lista_inver)

#Ordem decresccente:
print (lista_ordem[::-1])
    
