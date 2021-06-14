from application.model.entity.item import Produto

class CarrinhoDAO:
    def __init__(self):
        self.__carrinho_dict_list = []

    def adicionar_carrinho(self, produto: Produto):
        self.__carrinho_dict_list.append(produto)

    def remover_carrinho(self, produto):
        print(produto)
        for i in self.__carrinho_dict_list:
            if i['id'] == produto['id']:
                self.__carrinho_dict_list.remove(i)
                return self.__carrinho_dict_list

    def retornar_produto_lista(self):
        return self.__carrinho_dict_list
