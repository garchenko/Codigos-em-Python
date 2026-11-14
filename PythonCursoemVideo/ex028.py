# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint # biblioteca que permite gerar números inteiros aleatórios
from time import sleep # biblioteca que permite fazer o programa "dormir" por alguns segundos
print("-=" * 30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar qual é!")
print("-=" * 30)

numero_jogador = int(input("Em que número eu pensei? "))
numero_computador = randint(0, 5) #Faz o sorteio do número pelo computador

print("PROCESSANDO...")
sleep(3) # Faz o programa "dormir"

if numero_jogador == numero_computador:
    print("Parabéns! Você acertou!")
else:
    print(f"Errou, não foi dessa vez! Eu pensei no número {numero_computador}.")