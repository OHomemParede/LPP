sal = int(input("Salario: "))
por100 = int(input("Aumento(%): "))
print("Valor do Aumento: {}".format(sal*por100/100))
print("Valor do Novo Salario: {}".format(sal+(sal*por100/100)))
