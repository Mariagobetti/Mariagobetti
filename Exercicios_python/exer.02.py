funcionario = float(input('Qual é o salario do funcionario? R$'))
novo = funcionario + (funcionario * 15 / 100)
print('Um funcionario que ganhava R$ {:.2f} , com aumento de 15% passa a ganhar R$ {:.2f}.'.format(funcionario, novo))

#salario com aumento de 15%