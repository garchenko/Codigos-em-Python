# Crie um progama que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

valor = float(input("Quantos reais que você tem na carteira: R$ "))
dolar = 5.43
euro = 6.05
print(f"Com o valor de R$ {valor:.2f} \nVocê pode comprar US$ {valor / dolar:.2f} dólares \nOu pode comprar € {valor / euro:.2f} euros")