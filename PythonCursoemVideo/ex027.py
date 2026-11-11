# Faça um programa que leia  o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza | primeiro = Ana | Último = Souza

nome = input("Digite seu nome completo: ").strip()
nome = nome.split() # separa o nome em uma lista
print(f"Primeiro nome: {nome[0]}")
print(f"Último nome: {nome[len(nome)-1]}") # pega o último nome da lista