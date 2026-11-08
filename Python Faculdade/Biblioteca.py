class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        # Método auxiliar para formatar a exibição do livro na tela
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn})"

class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.livros = []  # Começa com uma lista vazia de livros

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")

    def remover_livro(self, isbn: str):
        # Procura o livro pelo ISBN na lista e o remove
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f"Livro '{livro.titulo}' removido com sucesso!")
                return
        print(f"Livro com ISBN {isbn} não encontrado.")

    def listar_livros(self):
        print(f"\n--- Livros na Biblioteca '{self.nome}' ---")
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            for livro in self.livros:
                print(f"- {livro}")

    def buscar_livro(self, titulo: str):
        #Busca um livro pelo titulo e retorna a instância do objeto
        #(ou None se não encontrar).
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

# Instanciando os livros
livro1 = Livro("Dom Casmurro", "Machado de Assis", "11111")
livro2 = Livro("O Cortiço", "Aluísio Azevedo", "0987654321")
livro3 = Livro("Memórias Póstumas", "Machado de Assis", "33333")

# Instanciando a biblioteca
minha_biblioteca = Biblioteca("Biblioteca Central")

# Adicionando os livros
minha_biblioteca.adicionar_livro(livro1)
minha_biblioteca.adicionar_livro(livro2)
minha_biblioteca.adicionar_livro(livro3)

# Listando todos os livros
minha_biblioteca.listar_livros()

# Removendo um livro pelo ISBN
minha_biblioteca.remover_livro("0987654321")

# Listando novamente após a remoção
minha_biblioteca.listar_livros()

# Testando a busca pelo título
resultado = minha_biblioteca.buscar_livro("Dom Casmurro")

if resultado:
    print(f"\nLivro encontrado: {resultado}")
else:
    print("\nLivro não encontrado.")