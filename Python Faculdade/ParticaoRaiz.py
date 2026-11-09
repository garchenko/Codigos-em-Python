#Programa em Python que mostra os números entre 1000 e 9999 cuja raiz quadrada seja igual à soma dos números formados pelos dois algarismos menos significativos e pelos dois algarismos mais significativos.

for num in range (1000,10000):
    menor = num % 100 #obtem o numero dos algarismos menos significativos
    maior = num // 100 #obtem o numero dos algarismos mais significativos
    raiz = menor + maior  #obtem a raiz

    if (raiz * raiz ) == num: #valida se a raiz gera o numero testado
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu ', num)