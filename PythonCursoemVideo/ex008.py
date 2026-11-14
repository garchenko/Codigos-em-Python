# Escreva um programa que leia um valor em metros e o exiba convertido em de quilômetros até milímetros.

metros = float(input("Digite um valor em metros: "))
print(f"O valor digitado é {metros}m \nConvertido em quilômetros é {metros / 1000:.3f}km \nConvertido em hectômetros é {metros / 100:.0f}hm \nConvertido em decâmetros é {metros / 10:.0f}dam \nConvertido em decímetros é {metros * 10:.0f}dm \nConvertido em centímetros é {metros * 100:.0f}cm \nConvertido em milímetros é {metros * 1000:.0f}mm")