salario =float(input("Qual é o salário do funcionário? R$"))
if salario <=1250:
    novo = salario +(salario *15/100)
else:
    novo = salario +(salario *10/100)
print("O salário do funcionário com aumento será: R${:.2f}".format(novo))
