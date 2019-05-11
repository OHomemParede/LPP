var = input("Digite um valor entre 0 e 10: ")
while var.isalnum()==False or var.isalpha() or var.isalpha()==False and var.isdigit()==False or int(var)>10 or int(var)<0:
    var = input("Digite um valor entre 0 e 10: ")
