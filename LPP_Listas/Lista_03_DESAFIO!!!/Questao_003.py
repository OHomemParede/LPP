while True:
    n = int(input("Digite um natural: "))
    x=2
    while n%x!=0:
        x=x+1
    
    print("primo" if x==n else "Não primo")
      
