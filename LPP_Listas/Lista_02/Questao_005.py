num1 = int(input("Primeiro Número: "))
num2 = int(input("Segundo Número: "))
num3 = int(input("Terceiro Número: "))

if num1>num2 and num1>num3:
    print("Maior Número: ",num1)
    if num2<num3:
        print("Menor Número: ",num2)
    if num2>num3:
        print("Menor  Número: ",num3)

if num2>num1 and num2>num3:
    print("Maior Número: ",num2)
    if num1<num3:
        print("Menor Número: ",num1)
    if num1>num3:
        print("Menor Número: ",num3)

if num3>num1 and num3>num2:
    print("Maior Número: ",num3)
    if num1<num2:
        print("Menor Número: ",num1)
    if num1>num2:
        print("Menor Número: ",num2)
