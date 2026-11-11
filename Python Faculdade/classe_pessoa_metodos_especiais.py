from datetime import datetime

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    # Método de classe: calcula a idade com base no ano atual e cria o objeto
    @classmethod
    def apartiranonasc(cls, nome: str, ano_nascimento: int):
        ano_atual = datetime.now().year
        idade = ano_atual - ano_nascimento
        return cls(nome, idade)  # Retorna uma nova instância de Pessoa

    # Método estático: apenas verifica uma regra lógica sem depender de dados internos
    @staticmethod
    def ehmaior(idade: int) -> bool:
        return idade >= 18

# 1. Instanciando diretamente com o construtor padrão (__init__)
pessoa1 = Pessoa("Ventury", 62)
print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade}")
print(f"É maior de idade? {Pessoa.ehmaior(pessoa1.idade)}")

print("-" * 30)

# 2. Instanciando via método de classe (passando ano de nascimento)
pessoa2 = Pessoa.apartiranonasc("LUG", 2013)
print(f"Nome: {pessoa2.nome}")
print(f"Idade: {pessoa2.idade}")
print(f"É maior de idade? {Pessoa.ehmaior(pessoa2.idade)}")