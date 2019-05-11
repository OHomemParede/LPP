mer = int(input("Preço da Mercadoria: "))
por100 = int(input("Desconto(%): "))

print("Valor Do Desconto: ", mer*por100/100)

print("Novo Preço: ", mer-(mer*por100/100))
