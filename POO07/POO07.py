
class Agenda:
    def __init__(self):
        self.contatos = []
        self.preencherAgenda()

    def preencherAgenda(self):
        validador = 1

        if int(input("Deseja adicionar contatos?\nSe não digite 0\nSe Sim digite 1\n")) == 0:
            return

        while validador == 1:
            self.adicionarContato()
            validador = int(input(f"\nDeseja adicionar mais contatos? \nSe não digite 0\nSe Sim digite 1\n"))

        self.imprimir()

    def adicionarContato(self):
        nome = input("Informe o nome do contato: ")
        numero = input("Informe o numero de telefone: ")

        self.contatos.append(Contato(nome, numero))

    def imprimir(self):
        print("Contatos")

        for contato in self.contatos:
            print(f"Nome: {contato.nome} Telefone: {contato.telefone}")

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

agenda = Agenda()
