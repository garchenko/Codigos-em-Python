#Crie um progama que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
num = float(input("Digite um número real: "))
print(f"O número digitado foi {num}.\nSua porção inteira é {trunc(num)}")

# Também pode ser feito com a função INT sem precisar importar biblioteca math

# num = float(input("Digite um número real: "))
# print(f"O número digitado foi {num}.\nSua porção inteira é {int(num)}")