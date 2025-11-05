#jogo da adivihação de números
from random import randint
from time import sleep
computador = randint(0,5) # faz o computador "pensar"
print("-=-"*20)
jogador = int(input("Em que número eu pensei entre 0 e 5?")) #Jogador tenta adivinhar
print("Processando....")
sleep(3)
if jogador == computador:
    print("Parabéns! Você me venceu")
else:
    print("Ganhei! Eu pensei no número {} e não no {}".format(computador ,jogador))
    #Estrutura condicional composta para o jogo da adivinhação usando if e else 


