num = list(input("DIgite um numero: "))
x = 1
var = []
while x<=len(num):
    var.append(num[x*-1])
    x=x+1
print(''.join(var))
