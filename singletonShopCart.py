class Carrinho:

    __instance = None

    def __init__(self):
        if Carrinho.__instance is None:
            Carrinho.__instance = self
            self.items = []
        else:
            raise Exception("Esta classe é um singletonn")
        
    @staticmethod
    def get_instance():
        if not Carrinho.__instance:
            Carrinho()
        
        return Carrinho.__instance
    
    def add_item(self, item):
        self.items.append(item)

    def get_item(self):
        return self.items


class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


#cliente:

#Utilizando o Singleton para criar o carrinho:
carrinho1 = Carrinho.get_instance()

#Criar os produtos:
produto1 = Produto("Banana", 4.00)
produto2 = Produto("Maçã", 7.99)
produto3 = Produto("Melão", 5.89)
produto4 = Produto("Repolho", 3.79)
produto5 = Produto("Água", 3.79)
produto6 = Produto("Linguiça", 3.79)

#Adicionar itens no carrinho:
carrinho1.add_item(produto1)
carrinho1.add_item(produto2)
carrinho1.add_item(produto3)
carrinho1.add_item(produto4)
carrinho1.add_item(produto5)
carrinho1.add_item(produto6)

#Exibindo a lista total dos carrinhos:
print("----------- Carrinho 1 -----------")
for item in carrinho1.get_item():
    print(item.nome, " - ", item.preco)
    numItens = numItens+1
    total = total + item.preco

