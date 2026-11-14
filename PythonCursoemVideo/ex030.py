# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print("=" * 40)
print("Analisador de números pares e ímpares")
print("=" * 40)

número = int(input("Digite um número qualquer: "))

if número % 2 == 0: #verifica se o resto da divisão por 2 é igual a 0
    print(f"O número {número} é PAR.")
else:
    print(f"O número {número} é ÍMPAR.")
