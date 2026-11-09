# Preço dos itens
hamburguer = 10.50
batata_frita = 4.00
refrigerante = 3.00

# Quantidade de itens pedidos pelo cliente
quantidade_hamburguer = int(input("Digite a quantidade de hambúrgueres desejados: "))
quantidade_batata = int(input("Digite a quantidade de batatas fritas desejadas: "))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerantes desejados: "))

# Cálculo do total de itens pedidos
preco_total = (hamburguer * quantidade_hamburguer) + (batata_frita * quantidade_batata) + (refrigerante * quantidade_refrigerante)

# Preço final para o cliente
print("O preço total do seu pedido é: R$", preco_total)