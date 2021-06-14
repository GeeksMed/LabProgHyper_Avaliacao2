import json
from application import app
from flask import Flask, render_template, request, url_for, jsonify
from application.model.entity.item import Produto
from application.model.entity.price import Price
from application.model.dao.itensDAO import ProdutosDAO
from application.model.dao.carrinhoDAO import CarrinhoDAO
carrinho_list = CarrinhoDAO()


@app.route("/", methods=['GET'])
def home():
    produto_json = open(r'application\controller\json\data.json', 'r')
    produto_json = json.load(produto_json)
    produtosDAO = ProdutosDAO(produto_json)
    produtos_list = produtosDAO.retornar_produto_lista()
    return render_template("index.html", produtos_list=produtos_list, carrinho_list=carrinho_list.retornar_produto_lista())


@app.route("/inserir/<int:id>", methods=['GET'])
def inserir(id):
    produto_json = open(r'application\controller\json\data.json', 'r')
    produto_json = json.load(produto_json)
    produtosDAO = ProdutosDAO(produto_json)
    produtos_list = produtosDAO.retornar_produto_lista()
    for produto in produtos_list:
        if produto['id'] == id:
            carrinho_list.adicionar_carrinho(produto)
            return render_template("index.html", produtos_list=produtos_list, carrinho_list=carrinho_list.retornar_produto_lista())
    return render_template("index.html", produtos_list=produtos_list, carrinho_list=carrinho_list.retornar_produto_lista()), 404

@app.route("/remover/<int:id>", methods=['GET'])
def remover(id):
    produto_json = open(r'application\controller\json\data.json', 'r')
    produto_json = json.load(produto_json)
    produtosDAO = ProdutosDAO(produto_json)
    produtos_list = produtosDAO.retornar_produto_lista()
    for produto in produtos_list:
        if produto['id'] == id:
            carrinho_list.remover_carrinho(produto)
            return render_template("index.html", produtos_list=produtos_list,
                                   carrinho_list=carrinho_list.retornar_produto_lista())
    return render_template("index.html", produtos_list=produtos_list,
                           carrinho_list=carrinho_list.retornar_produto_lista()), 404