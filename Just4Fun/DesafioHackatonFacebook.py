def hack(n,k):
  lista = []

  def conta_uns(x):return x.count('1')

  lista = [bin(e) for e in range(2**n-1)]
  lista = sorted(lista,key=conta_uns, reverse=True)
 

  return lista
