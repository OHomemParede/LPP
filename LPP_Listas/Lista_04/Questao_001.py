from random import randint

lista = [randint(1,100) for k in range(10)]
print(lista)

maior = lista[0]
menor = lista[0]
x = 0

while x<len(lista):
    
    if maior<lista[x]: maior = lista[x]
    if menor>lista[x]: menor = lista[x]
    
    x = x+1
    
print(maior)
print(menor)
