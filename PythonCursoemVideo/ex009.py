# Faça um progama que leia um numero inteiro e mostre na tela a sua tabuada.

num = int(input("Digite um número inteiro: "))
print(f"A tabuada do número {num} é: ")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")