num = int(input("Digite um numero: "))

x=2 
div_primos = []

while True:
    if num%x==0 and num/x!=1:
        div_primos.append(x)
        num = num/x
    elif num%x==0 and num/x==1:
        div_primos.append(x)
        break
    else:
        x=x+1
print(div_primos)



##num = int(input("Digite um numero: "))
##
##for k in range(2, num):
##    while num % k == 0:
##        print(k)
##        num = num / k
