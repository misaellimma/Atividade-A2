from datetime import date

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, codLivro, autor, titulo):
        self.codLivro = codLivro
        self.autor = autor
        self.titulo = titulo

    def toString(self):
        return f"cod {self.codLivro} Titulo: {self.titulo}, Autor: {self.autor}"

class Emprestimo:
    def __init__(self, pessoa):
        self.dataEmprestimo = date.today()
        self.dataDevolucao = ""
        self.livros = []
        self.pessoa = pessoa

    def adicionarLivro(self, livro):
        self.livros.append(livro)

    def devolver(self):
        self.dataDevolucao = date.today()

    def imprimir(self):
        print("\nEmprestimo")
        print(f"Nome: {self.pessoa.nome}")
        print(f"Data emprestimo: {self.dataEmprestimo}")
        print(f"Data devolução: {self.dataDevolucao}")
        print("Livros")
        for livro in self.livros:
            print(livro.toString())

class Livraria:
    def __init__(self):
        self.lancarEmprestimo()

    def lancarEmprestimo(self):
        def obterPorCodLivro(lista, codLivro):
            for livro in lista:
                if (livro.codLivro == codLivro):
                    return livro

        def imprimirLivros(lista):
            print("\nLivros")
            for livro in lista:
                print(livro.toString())

        pessoa = Pessoa(input("informe um nome: "))

        listaLivros = []
        listaLivros.append(Livro(1, "charles", "o poder do habito"))
        listaLivros.append(Livro(2, "daniel", "rapido e devagar"))

        imprimirLivros(listaLivros)
        i = 1

        emprestimo = Emprestimo(pessoa)

        while i == 1:
            codLivro = int(input(f"informe o cod do livro para emprestimo: "))
            emprestimo.adicionarLivro(obterPorCodLivro(listaLivros, codLivro))
            i = int(input(f"\nDeseja adicionar mais livros? \nSe não digite 0\nSe Sim digite 1\n"))

        emprestimo.imprimir()

        devolverLivroValidacao = int(input(f"\nDeseja devolver os livros? \nSe não digite 0\nSe Sim digite 1\n"))

        if devolverLivroValidacao == 1:
            emprestimo.devolver()

        emprestimo.imprimir()

principal = Livraria()