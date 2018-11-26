vetor_lista = []
print("Digite os Valores inteiros do seu Vetor seguindo os seguintes parâmetros:"
     , "Um número inteiro por vez, seguido da tecla Enter. Para encerrar o vetor, digite: 0")
while True:
    n = input()
    if (int(n) != 0):
        vetor_lista.append(n)
    else:
        break
media = 0
i = 0
for (n) in vetor_lista:
    if (int(n)%2) == 0:
        media = media + int(n)
        i = i + 1
if i != 0:
    print ("%.2f" %int(media/i))
else:
    print("-1")
