from random import randint

lista = [randint(1, 100) for k in range(20)]

par = []
impar = []

x = 0

while x < len(lista):
    if lista[x]%2==0:
        par.append(lista[x])
    else:
        impar.append(lista[x])
    x = x+1
print("""Lista: {}
par: {}
impar: {}""".format(lista, par, impar))

