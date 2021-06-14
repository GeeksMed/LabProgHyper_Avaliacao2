from application.model.entity.item import Produto

class ProdutosDAO:
    def __init__(self, produto_json):
        produto_dict_list = []
        for produto in produto_json['items']:
            produto = produto['product']
            produto_append = Produto(produto['id'], produto['name'], produto['images'], produto['price'])
            produto_dict_list.append(produto_append.toDict())
        self.__produto_dict_list = produto_dict_list

    def retornar_produto_lista(self):
        return self.__produto_dict_list


