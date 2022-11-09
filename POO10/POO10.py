import locale
from datetime import date

class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.dataAbertura = date.today()

    def getSaldo(self):
        return self.saldo

    def setSaldo(self, valor):
        self.saldo = valor

    def getDataAbertura(self):
        return self.dataAbertura

    def obterDataAberturaFormatada(self):
        return f"{self.dataAbertura.day}/{self.dataAbertura.month}/{self.dataAbertura.year}"

    def obterSaldoFormatado(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self.saldo, grouping=True)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Erro: Valor do saque não pode ser maior que saldo atual")
            return
        self.saldo -= valor

    def imprimir(self):
        print(f"Conta Bancaria")
        print(f"Saldo da conta: {self.obterSaldoFormatado()}")
        print(f"data da abertura da conta: {self.obterDataAberturaFormatada()}")

class Banco:
    def __init__(self):
        validacao = int(input(f"\nDeseja criar uma conta Bancaria? \nSe não digite 0\nSe Sim digite 1\n"))
        if validacao == 0:
            return

        contaBancaria = ContaBancaria()
        contaBancaria.imprimir()

        validacao = int(input(f"\nDeseja realizar um depósito? \nSe não digite 0\nSe Sim digite 1\n"))

        if validacao == 1:
            valor = float(input(f"informe o valor a ser depositado: "))
            contaBancaria.depositar(valor)
            contaBancaria.imprimir()

        validacao = int(input(f"\nDeseja realizar um saque? \nSe não digite 0\nSe Sim digite 1\n"))

        if validacao == 1:
            valor = float(input("informe o valor a ser sacado: "))
            contaBancaria.sacar(valor)
            contaBancaria.imprimir()

banco = Banco()