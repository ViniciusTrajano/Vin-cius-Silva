n = int(input('Digite Um número inteiro positivo: '))
def seq_par(num):
    if num //2 != 0:
        print(n - num)
        return seq_par(num - 2)
    else:
        print (n - num)
seq_par(n)
