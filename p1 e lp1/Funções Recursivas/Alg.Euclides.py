n = int(input())
texto = 'MDC({},{}) = {}'
############################################
#Função de MDC EUCLIDIANA

def euclides(A,D):
    if A%D == 0:
        return D
    return euclides(D,(A%D))
############################################    
for i in range(n):
    lista = input().split()
    a = int(lista[0])
    b = int(lista[1])
    print(texto.format(a,b,euclides(a,b)))
