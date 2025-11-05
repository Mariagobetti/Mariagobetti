from time import sleep
distancia = float(input("Qual é a distância da viagem em Km ?"))
print("Você está prestes a começar uma viagem de {} km".format(distancia))
print("Calculando o preço da sua passagem...")
sleep(3)
if distancia <=200:
    preço = distancia * 0.45
else: 
    preço = distancia * 0.50
    print(" O preço da sua passagem será de R$ {:.2f}".format(preço))
    #Calculando o preço da passagem de uma viagem com if e else e usando a biblioteca time com a função sleep 


