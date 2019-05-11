import requests

#import urllib.request
#import json
#from pprint import pprint 

url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'

data = requests.get(url).json()

#resp = urllib.request.urlopen(url).read()
#data = json.loads(resp.decode('utf-8'))
#pprint(data['value']['categories'])
print (data['value']['joke'])


#json = java script object notation
#tipo chave valor; posso converter para dicionario.
#ideograma

lista = 'Daneil Jose Gustavo Christian Talita Mariana Leo Bianca TiaElene Kain'.split()
def troca(l):
    l2 = lista
    l2[0] = 'DANIEL'
    return l2
