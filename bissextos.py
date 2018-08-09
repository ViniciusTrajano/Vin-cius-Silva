a1=int(input())
a2=int(input())
i=0
for ano in range (a1,(a2+1)):
    if (ano%4)==0:
        print(ano)
        i=i+1
        
if i==0:
    print("-1")
