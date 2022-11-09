class Produto:
    def __init__(self, codProduto, descricao, preco, quantidadeEstoque):
        self.codProduto = codProduto
        self.descricao = descricao
        self.preco = preco
        self.quantidadeEstoque = quantidadeEstoque

    def toString(self):
        return f"{self.codProduto} - {self.descricao} R$ {self.preco}"

class PedidoItem:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def toString(self):
        return f"{self.produto.codProduto} - {self.produto.descricao} Qtde: {self.quantidade} R$ {self.produto.preco * self.quantidade}"

class FormaPagamento:
    def __init__(self, codFormaPagamento, descricao):
        self.codFormaPagamento = codFormaPagamento
        self.descricao = descricao

    def toString(self):
        return f"{self.codFormaPagamento} - {self.descricao}"

class Pedido:
    def __init__(self):
        self.pedidoItens = []
        self.formaPagamento = ""
        self.cliente = ""

    def adicionarPedidoItem(self, pedidoItem):
        self.pedidoItens.append(pedidoItem)

    def setFormaPagamento(self, formaPagamento):
        self.formaPagamento = formaPagamento

    def setCliente(self, cliente):
        self.cliente = cliente

    def toStringItens(self):
        for item in self.pedidoItens:
            print(f"{item.produto.descricao} Qtde: {item.quantidade} Valor total: R$ {item.produto.preco * item.quantidade}")

    def imprimirPedido(self):
        print("\nItens do Pedido:")
        valorTotal = 0

        for item in self.pedidoItens:
            print(f"{item.produto.descricao} Qtde: {item.quantidade} Valor total: R$ {item.produto.preco * item.quantidade}")
            valorTotal += item.produto.preco * item.quantidade

        print(f"\nForma de Pagamento: {self.formaPagamento.descricao}")
        print(f"Valor total do pedido: {valorTotal}")

class Supermercado:
    def __init__(self):
        self.realizarPedido()

    def realizarPedido(self):
        addPedidoItem = 1

        def obterPorCodProduto(listaProdutos, codProduto):
            for produto in listaProdutos:
                if (produto.codProduto == codProduto):
                    return produto

        def imprimirProdutos(listaProdutos):
            print("\nProdutos")
            for produto in listaProdutos:
                print(produto.toString())

        def imprimirItens(pedido):
            print("\nItens do pedido:")
            pedido.toStringItens()

        def imprimirFormaPagamento(lista):
            print("\nForma de Pagamento:")
            for formaPagamento in lista:
                print(formaPagamento.toString())

        def obterPorCodFormaPagamento(listaFormaPagamento, codFormaPagamento):
            for formaPagamento in listaFormaPagamento:
                if (formaPagamento.codFormaPagamento == codFormaPagamento):
                    return formaPagamento

        fazerPedido = int(input("Deseja fazer um pedido?\nSe não digite 0\nSe Sim digite 1\n"))

        if (fazerPedido == 0):
            return

        listaProdutos = []
        listaProdutos.append(Produto(1, "Suco", 10.00, 50))
        listaProdutos.append(Produto(2, "Arroz", 20.00, 100))
        listaProdutos.append(Produto(3, "Feijão", 5.00, 200))

        listaFormaPagamento = []
        listaFormaPagamento.append(FormaPagamento(1, "Dinheiro"))
        listaFormaPagamento.append(FormaPagamento(2, "Cheque"))
        listaFormaPagamento.append(FormaPagamento(3, "Cartão"))

        pedido = Pedido()

        while addPedidoItem == 1:
            imprimirProdutos(listaProdutos)
            codProduto = int(input(f"Selecione o cod do produto: "))
            quantidade = int(input(f"informe a quantidade do produto: "))

            pedido.adicionarPedidoItem(PedidoItem(obterPorCodProduto(listaProdutos, codProduto), quantidade))
            imprimirItens(pedido)
            addPedidoItem = int(input(f"\nDeseja adicionar mais produtos? \nSe não digite 0\nSe Sim digite 1\n"))

        imprimirFormaPagamento(listaFormaPagamento)

        codPagamento = int(input("informe um cod forma de pagamento: "))
        pedido.setFormaPagamento(obterPorCodFormaPagamento(listaFormaPagamento, codPagamento))
        pedido.imprimirPedido()

supermercado = Supermercado()
