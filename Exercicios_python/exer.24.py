velocidade = float(input("Qual é a velocidade atual do carro?"))
if velocidade > 80:
    print("Você foi multado por excesso de velocidade!")
    multa =(velocidade - 80) *7
    print("Você deve pagar uma multa de R$ {:,.2f}!".format(multa))
else:
    print("Você está dentro do limite de velocidade. Dirija com segurança")
    #Verificando se o motorista foi multado por excesso de velocidade com if e else 