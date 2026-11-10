# Entrada e conversão dos dados
num_int = int(input("Digite um número inteiro: "))
num_float = float(input("Digite um número de ponto flutuante: "))

# Para booleano, converte a entrada para minúsculas e verifica se é "true"
entrada_bool = input("Digite um valor booleano (True ou False): ")
val_bool = entrada_bool.strip().lower() == "true"

# Exibição formatada
print("\nValores convertidos:")
print(f"- Número inteiro: {num_int} (tipo: {type(num_int).__name__})")
print(f"- Número de ponto flutuante: {num_float} (tipo: {type(num_float).__name__})")
print(f"- Valor booleano: {val_bool} (tipo: {type(val_bool).__name__})")