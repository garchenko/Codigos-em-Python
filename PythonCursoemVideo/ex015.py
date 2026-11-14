#Escreva um progama que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

# Solicita ao usuário a quantidade de km percorridos
km = float(input("Digite a quantidade de km percorridos: "))

# Solicita ao usuário a quantidade de dias alugados
dias = int(input("Digite a quantidade de dias alugados: "))

# Calcula o preço a pagar
preco_total = (dias * 60) + (km * 0.15)

# Exibe o resultado
print(f"O preço total a pagar é: R${preco_total:.2f}")