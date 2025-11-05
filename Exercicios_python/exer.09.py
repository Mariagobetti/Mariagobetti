co=float(input("Comprimento do cateto oposto:"))
ca=float(input("Comprimento do cateto adjacente:"))
hi=(co**2+ca**2)**(1/2)
print("A hipotnusa vai medir {:.2f}".format(hi))
#Calculando a hipotenusa de um triângulo retângulo usando a fórmula de pitágoras

import math
co=float(input("Comprimento do cateto oposto:"))
ca=float(input("Comprimento do cateto adjacente:"))
hi=math.hypot(co,ca)
print("A hipotenusa vai medir {:.2f}".format(hi))
#Calculando a hipotenusa de um triângulo retângulo usando a função hypot da biblioteca math
