from random import randint
vetor1 = [randint(1, 100) for k in range(10)]
vetor2 = [randint(1, 100) for k in range(10)]

vetor3 = []
x = 0
while x<10:
    
    vetor3.append(vetor1[x])
    vetor3.append(vetor2[x])
    x = x+1

print("""1° vetor: {}
2° vetor: {}
3° vetor: {}""".format(vetor1, vetor2, vetor3))
