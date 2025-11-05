nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")

# deixa tudo minúsculo para evitar erros de maiúsculas/minúsculas
if "silva" in nome.lower():
    print("Seu nome TEM Silva.")
else:
    print("Seu nome NÃO tem Silva.")

#Verificando se o nome tem o sobrenome "Silva"
