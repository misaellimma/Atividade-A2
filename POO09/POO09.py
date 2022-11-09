
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.pai = ""
        self.mae = ""

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def setPai(self, pai):
        self.pai = pai

    def setMae(self, pessoa):
        self.mae = pessoa

    def imprimir(self):
        print("\nFamilia")
        print(f"Seu nome: {self.nome} \nSua idade: {self.idade}")

        if self.mae != "":
            print(f"\nNome da mãe: {self.mae.getNome()} \nIdade da mãe: {self.mae.getIdade()}")

        if self.pai != "":
            print(f"\nNome do pai: {self.pai.getNome()} \nIdade do pai: {self.pai.getIdade()}")


class arvoreGenealogica:
    def __init__(self):
        nome = input("informe seu nome: ")
        idade = input("informe sua idade: ")

        pessoa = Pessoa(nome, idade)

        informarPai = int(input(f"\nDeseja informar o pai? \nSe não digite 0\nSe Sim digite 1\n"))

        if informarPai == 1:
            nomePai = input("informe o nome do pai: ")
            idadePai = input("informe a idade do pai: ")

            pessoa.setPai(Pessoa(nomePai, idadePai))

        informarMae = int(input(f"\nDeseja informar a mae? \nSe não digite 0\nSe Sim digite 1\n"))

        if informarMae == 1:
            nomeMae = input("informe o nome da mãe: ")
            idadeMae = input("informe a idade da mãe: ")

            pessoa.setMae(Pessoa(nomeMae, idadeMae))

        pessoa.imprimir()

arvore = arvoreGenealogica()