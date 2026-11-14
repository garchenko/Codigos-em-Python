# Crie uma programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Digite o nome de uma cidade: ")).strip()

print(cidade[:5].upper() == "SANTO") #verifica se os 5 primeiros caracteres da string são iguais a "SANTO" e retorna True ou False