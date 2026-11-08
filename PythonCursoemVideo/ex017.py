#Faça um progama que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print(f"O comprimento da hipotenusa é {hi:.2f}")

# O cálculo da hipotenusa também pode ser feito utilizando a fórmula: hi = (co ** 2 + ca ** 2) ** (1/2), sem precisar importar a biblioteca math.