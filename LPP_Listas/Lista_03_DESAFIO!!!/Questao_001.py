n = int(input("Digite um valor n: "))

x = 0
while x * (x+1) * (x+2) < n:
    x += 1
print(x * (x+1) * (x+2) == n)

