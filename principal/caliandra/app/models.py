class Produto:
    def __init__(self, nome, preco, descricao, img):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.img = img

    def __str__(self):
        return f"Produto:{self.img} {self.nome}, Preço: {self.preco}, Descrição: {self.descricao}"