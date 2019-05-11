A = 80000
B = 200000
ano = 0
while A < B:
    A = A+(A*0.03)
    B = B+(B*0.015)
    ano=ano+1
print("Em {} anos a população do país A terá ultrapassado a população do país B".format(ano))
