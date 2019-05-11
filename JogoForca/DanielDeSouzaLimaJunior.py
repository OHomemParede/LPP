#Daniel de Souza Lima Junior

from random import choice
import requests
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
palavras = requests.get(url).text.lower().split()


forca = [
'''
      +-----+
      |     |
            |
            |
            |
            |
   +--------+
 ''','''
      +-----+
      |     |
      0     |
            |
            |
            |
   +--------+
 ''','''
      +-----+
      |     |
      0     |
      |     |
            |
            |
   +--------+
 ''','''
      +-----+
      |     |
      0     |
      |\    |
            |
            |
   +--------+
 ''','''
      +-----+
      |     |
      0     |
     /|\    |
            |
            |
   +--------+
 ''','''
       +-----+
       |     |
       0     |
      /|\    |
        \    |
             |
    +-------+
 ''', '''
       +-----+
       |     |
       0     |
      /|\    |
      / \    |
             |
    +--------+
 ''']


def vitoriaLegal():
  print('''                        vv
                     vvv^^^^vvvvv
                 vvvvvvvvv^^vvvvvv^^vvvvv
        vvvvvvvvvvv^^^^^^^^^^^^^vvvvv^^^vvvvv
    vvvvvvv^^^^^^^^^vvv^^^^^^^vvvvvvvvvvv^^^vvv
  vvvv^^^^^^vvvvv^^^^^^^vv^^^^^^^vvvv^^^vvvvvv
 vv^^^^^^^^vvv^^^^^vv^^^^vvvvvvvvvvvv^^^^^^vv^
 vvv^^^^^vvvv^^^^^^vvvvv^^vvvvvvvvv^^^^^^vvvvv^
  vvvvvvvvvv^^^v^^^vvvvvv^^vvvvvvvvvv^^^vvvvvvvvv
   ^vv^^^vvvvvvv^^vvvvv^^^^^^^^vvvvvvvvv^^^^^^vvvvvv
     ^vvvvvvvvv^^^^vvvvvv^^^^^^vvvvvvvv^^^vvvvvvvvvv^v
        ^^^^^^vvvv^^vvvvv^vvvv^^^v^^^^^^vvvvvv^^^^vvvvv
 vvvv^^vvv^^^vvvvvvvvvv^vvvvv^vvvvvv^^^vvvvvvv^^vvvvv^
vvv^vvvvv^^vvvvvvv^^vvvvvvv^^vvvvv^v##vvv^vvvv^^vvvvv^v
 ^vvvvvv^^vvvvvvvv^vv^vvv^^^^^^_____##^^^vvvvvvvv^^^^
    ^^vvvvvvv^^vvvvvvvvvv^^^^/\@@@@@@\#vvvv^^^
         ^^vvvvvv^^^^^^vvvvv/__\@@@@@@\^vvvv^v
             ;^^vvvvvvvvvvv/____\@@@@@@\vvvvvvv
             ;      \_  ^\|[  -:] ||--| | _/^^
             ;        \   |[   :] ||_/| |/
             ;         \\ ||___:]______/
             ;          \   ;=; /
             ;           |  ;=;|
             ;          ()  ;=;|
            (()          || ;=;|
                        / / \;=;\
''')



def escolhe(): return choice(palavras)


def desenha(sorteada,erradas,certas):
  print(forca[len(erradas)])
  for s in sorteada:
    if s in certas: print(s, end = ' ')
    else:print('_', end=' ')


def chute(certas,erradas):
  while True:
    guess = input('Chute uma Letra: ').lower()
    if (len(guess)!=1 or not guess.isalpha() or guess.isdecimal()
        or guess in certas+erradas):
      print('chute inválido, digite outro')
    else:return guess


def jogar_novamente():
  return input('Você Gostaria de Jogar Novamente? ').lower() == 'sim'
  

def ganhou(certas,sorteada):return len(set(certas)) == len(set(sorteada))


#-------------------------------------------------------------------------

while True: #Quando o Jogo Começa
  sorteada = escolhe()
  certas = erradas = ''
  while True: #Quando a Partida Começa
    
    if ganhou(certas,sorteada):
      vitoriaLegal()
      print('\n'+'-='*10+'Você Ganhou!!!'+'-='*10+'\n')
      break
    desenha(sorteada,erradas,certas)
    
    print()#pulando uma linha :)
    if len(erradas) == len(forca)-1:print('Você perdeu!!!');break
    
    guess = chute(certas,erradas)
    
    if guess in sorteada: certas+=guess
    else: erradas+=guess
    
  if not jogar_novamente(): break

#---------------------------------------------------------------------------------
  
