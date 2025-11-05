num =int(input("Digite um número:"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
n = str(num)
print("Analisando o número {}".format(n))
print("Unidade: {}".format(u))
print("Dezena: {} ".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

#Separando os dígitos de um número inteiro e mostrando suas unidades,dezenas,cetenas e milhares

