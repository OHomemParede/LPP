import requests
from bs4 import BeautifulSoup as bs
##
##url = 'https://sismpconsultapublica.mpsp.mp.br/ConsultarDistribuicao/ObterProcedimentosPorMembro?Membro=1426&ClassificacaoTipoProcedimento=Todos'
##p = requests.get(url)
##
##s = bs(p.text, 'html.parser')
##lista = s.findAll('option')
##
##nomes = lista[1:-5]
##
##for name in nomes:
##    print(name.string, name['value'])

u = 'http://filiaweb.tse.jus.br/filiaweb/portal/relacoesFiliados.xhtml'
p = requests.get(u)
s = bs(p.text, 'html.parser')
itens = s.findAll('option')
for p in itens:
    print (p['value'])

partidos = itens[:-27] #correto
partidos = itens[14:16] #para não demorar...
ufs = itens[-27:] #correto
ufs = itens[-27:-25] #para não demorar
url = 'http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/filiados_'
from urllib.request import urlretrieve
for p in partidos:
    for uf in ufs:
        u = f'{url}{p["value"]}_{uf["value"]}.zip'
        file = f'{p["value"]}_{uf["value"]}.zip'
        print (file)
        urlretrieve (u, file)
