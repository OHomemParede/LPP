peso = int(input("Peso do Peixe(Kg): "))
multa = 0
if peso>50:
    multa = (peso-50)*4
    ex = peso-50
    print("excesso: ", ex, "Kg")
    print("Multa: R$", multa)
else:
    ex=0
    print("excesso: ",ex)
    print("Multa: ",multa)
