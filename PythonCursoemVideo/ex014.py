#Escreva um progama que converta uma temperatura digitada em C° e converta para F°

# Solicita ao usuário que insira a temperatura em Celsius
celsius = float(input("Digite a temperatura em Celsius: "))

# Converte a temperatura de Celsius para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibe o resultado
print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")