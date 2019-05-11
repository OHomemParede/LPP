##area = int(input("Metros Quadrados da Área: "))
##
###1 litro : 3 metros² --> 18litros : 54 metros² --> 1 lata : 18 litros --> 1 lata : 54 metros²
##
##while area%54!=0:
##    area=area+1
##
##lata = area/54
##valor = lata*80
##
##print("Quantidade de Latas: ",lata)
##print("Preço: ",valor)


area = int(input("Digite o Valor da Area a ser pintada: "))

if area%54!=0:
    lata = (area/54)+1    
else:
    lata = area/54
print("Qunatidade de Lata(s): ",int(lata))
print("Valor a ser pago: ",int(lata)*80)
