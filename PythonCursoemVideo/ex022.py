# Crie um programa que leia o nome de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome completo: ")).strip()
print("Nome em maiúsculas: ", nome.upper())
print("Nome em minúsculas: ", nome.lower())
print("Quantidade de letras (sem espaços): ", len(nome) - nome.count(" "))
print("Quantidade de letras no primeiro nome: ", nome.find(" ")) # Tambem pode ser feito com o nome.split()[0] para pegar o primeiro nome e depois len() para contar as letras.