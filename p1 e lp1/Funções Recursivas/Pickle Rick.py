N = int(input('Quantidade de horas que o Rick permaneceu como Pickle Rick:'))
def fib(n):
     if n <= 1:
         return n
     else:
         return fib(n-1) + fib(n-2)
print('{} mg/L'.format(fib(N)))
