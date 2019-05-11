lado_a = int(input("Lado A: "))
lado_b = int(input("Lado B: "))
lado_c = int(input("lado C: "))

if lado_a>lado_b+lado_c or lado_b>lado_a+lado_c or lado_c>lado_a+lado_b:
    print("com esses valores não é possivel ter um triãngulo")

elif lado_a == lado_b and lado_a == lado_c:
    print("Triãgulo Equilãtero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Triãngulo Isósceles")
else:
    print("Triãngulo Escaleno")
