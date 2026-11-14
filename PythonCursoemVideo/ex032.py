# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date # importando a biblioteca date para pegar o ano atual do usuario

print('=-' * 20)
print('Analisador de anos bissextos inteligente')
print('=-' * 20)

ano = int(input('Digite um ano para analisarmos: '))
ano_atual = date.today().year # verifica se o ano digitado é o ano atual do usuario

# verifica se o ano é bissexto
bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
print('-'*45)

# logica para saber se o ano é bissexto e compara passado, presente e futuro
if ano == ano_atual and bissexto:
    print(f'O ano {ano} é o atual e ele É BISSEXTO!')

elif ano == ano_atual and not bissexto:
    print(f'O ano {ano} é o ano atual e ele NÃO é BISSEXTO')

elif ano < ano_atual and bissexto:
    print(f'O ano {ano} já passou e ele foi BISSEXTO!')

elif ano < ano_atual and not bissexto:
    print(f'O ano {ano} já passou e ele NÃO foi BISSEXTO.')

elif ano > ano_atual and bissexto:
    print(f'O ano {ano} ainda vai chegar e ele SERÁ BISSEXTO!')
    
else:
    print(f'O ano {ano} ainda vai chegar e ele NÃO SERÁ BISSEXTO.')