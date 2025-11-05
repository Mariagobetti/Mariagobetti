from datetime import date
ano =int(input("Digite o ano que você quer analisar:"))
if ano ==0:
    ano = date.today().year
if (ano %4==0 and ano %100 !=0) or (ano %400==0):
    print("O ano {} é bissexto!".format(ano))
else:
    print("O ano {} não é bissexto!".format(ano))
    #Verificando se o ano digitado é bissexto ou não com if e else 
