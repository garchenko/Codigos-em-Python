# Faça um progama que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto: R$"))
print(f"O preço do produto com 5% de desconto é de R${preco * 0.95:.2f}")

#Tambem pode fazer o calculo dessa maneira: 
# preco - (preco * 5 / 100)