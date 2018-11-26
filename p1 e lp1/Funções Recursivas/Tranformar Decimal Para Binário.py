n=int(input())
#########################################
#Função para binários:

li=[]
def bin(num,l):
    if num >= 2:
        l.append(num%2)
        return bin(num//2,l)
    else:
        return l.append(num%2)
    
#########################################
    
bin(n,li)
li.reverse()
for i in li:
    print(i)
