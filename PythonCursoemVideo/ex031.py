# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

print("-=-"*10)
print("Calculadora de preço de passagem")
print("-=-"*10)

distancia = float(input("Digite a distãncia da viagem em Km: "))

if distancia <= 200: 
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# o calculo tambem pode ser feito de uma forma simplificada:
# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print("-=-"*20)
print(f"Uma viagem de {distancia:.0f}Km, terá o preço da passagem de R${preco:.2f}")
