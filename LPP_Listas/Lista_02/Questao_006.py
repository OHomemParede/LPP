sal_por_hora = int(input("Qual seu salario por hora? "))
horas_trab = int(input("Número de horas trabalhadas no mês: "))


sal_mes = sal_por_hora*horas_trab

print("Salário Bruto: R${}".format(sal_mes))

print("IR: R$ {}".format(sal_mes*0.11))

print("INSS: R${}".format(sal_mes*0.08))

print("Sindicato: R$ {}".format(sal_mes*0.05))


sal_mes = sal_mes-(sal_mes*(0.11+0.08+0.05))
print("Salário Liquido: R$ {}".format(sal_mes))



