# Definindo os preços unitários dos produtos (Atribuição)
preco_arroz = 5.50
preco_feijao = 8.00
preco_leite = 4.50

# Entrada de dados: solicitando a quantidade comprada de cada item
qtd_arroz = int(input("Digite a quantidade de pacotes de arroz: "))
qtd_feijao = int(input("Digite a quantidade de pacotes de feijão: "))
qtd_leite = int(input("Digite a quantidade de caixas de leite: "))

# Cálculo dos subtotais e do total final
subtotal_arroz = qtd_arroz * preco_arroz
subtotal_feijao = qtd_feijao * preco_feijao
subtotal_leite = qtd_leite * preco_leite

total_compra = subtotal_arroz + subtotal_feijao + subtotal_leite

# Saída de dados formatada
print("\n--- RESUMO DA COMPRA ---")
print(f"Arroz: {qtd_arroz}x R$ {preco_arroz:.2f} = R$ {subtotal_arroz:.2f}")
print(f"Feijão: {qtd_feijao}x R$ {preco_feijao:.2f} = R$ {subtotal_feijao:.2f}")
print(f"Leite: {qtd_leite}x R$ {preco_leite:.2f} = R$ {subtotal_leite:.2f}")
print("-" * 24)
print(f"TOTAL A PAGAR: R$ {total_compra:.2f}")