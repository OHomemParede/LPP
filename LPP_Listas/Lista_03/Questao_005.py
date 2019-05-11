print("***Algoritmo de Euclides***")

numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("DIgite o segundo numero:"))

resto = 1#entrando no loop

while resto != 0:
    
    resto = numero_1 % numero_2
    mdc = numero_2
    
    numero_1 = numero_2
    numero_2 = resto

    
print("MDC = {}".format(mdc))
