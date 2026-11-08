# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o salário do funcionário: R$"))
print(f"O aumento de 15% no salário do funcionário é de R${salario * 0.15:.2f} \nO novo salário do funcionário é de R${salario * 1.15:.2f}")

#Tambem pode fazer o calculo dessa maneira:
# salario + (salario * 15 / 100)