#A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 

user_num = int(input("Digite um numero inteiro: "))

z = 1
y = 0

x = 1
while x <= user_num:
    F_num = y + z 
    print(F_num)
    
    z = y
    y = F_num 
    
    x=x+1

print("\n{}° elemento:".format(user_num),F_num)
