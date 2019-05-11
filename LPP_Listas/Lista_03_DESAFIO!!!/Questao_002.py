#NOTAS: 50, 20, 10, 5, 2, 1
#OBJTIVO: Dar o minimo de NOTAS.

valor_conta = int(input("Valor a ser pago: "))
valor_pagamento = int(input("Valor do pagamento: "))

troco = valor_pagamento - valor_conta

notas = [50, 20, 10, 5, 2, 1]

y = 0

while troco!=0:
    x = troco//notas[y]
    if x != 0:
        troco = troco - notas[y]*x
        print(x,'nota de',notas[y])
    y=y+1
