import pandas
def multiplonine(num):
    
    i=num
    sum=0
    suma=11
    j=0

    while num>0:
        (num)
        sum+=num%10
        num=int(num/10)
        if sum >=10:
            num1=sum
            aux=0
            aux+=num1%10
            num1=int(num1/10)
            aux+=num1%10
            sum=aux
        j+=1
        ("suma",sum, "num", num, "digitos", j)
            
    suma=sum
    num=suma
    (suma)
    primero=int(i/10**(j-1))

    if suma == 9 or suma==0:
        fullnum=str(int((primero)*10**j+(i%10**(j-1))))
    else:
        add=9-suma
        if add>=int(primero):
            num=0
            n=i
            for k in range(j, 0, -1):
               k=k-1
               digito=int(n/10**(k))
               num+=digito
               n=n%10**(k)
               num*=10
               print("digito", digito, "numero", num, "add", add, "original", i, "n", n)
               if digito>add:
                num/=10
                print(k)
                print(((int((num)*10**(k-1))*10**j)+ int(num%10**(k+1)))+(add*10**(k+1)))
                print(num%10**(k+1))
                print("num que saca", str(int((((num)*10**(k-1))*10**j)+(num%10**(k+1)))))
                break
            fullnum=str(i*10+add) #se pone al final aca esta el problema

        else:fullnum=(add*(10**j))+i #se pone al inicio

    return fullnum

if __name__ == '__main__':    
    t = int(input().strip())
    lista=[]
    
    for j in range(t):
        p = str(input().strip())
        #lista.append(str("Case #"+str(j+1)+": ")+ str(multiplonine(int(p))))
        print(("Case #"+str(j+1)+":"), multiplonine(int(p)))

    p=pandas.DataFrame(lista)
    #p.to_excel("dataset1.xlsx")

""" num=1567894564751321546

i=num
sum=0
suma=11
while suma>10:
    sum=0
    while num>0:
        print(num)
        sum+=num%10
        num=int(num/10)    
    suma=sum
    num=suma
    print(suma)

if suma == 9:
    fullnum=str("ya es multiplo")
else:
    add=9-suma
    if add>=int(str(i)[0]):fullnum=str(i)+str(add)
    else:fullnum=str(add)+str(i)

print(fullnum) """