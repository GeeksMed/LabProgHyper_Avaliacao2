import json
from application import app
from flask import Flask, render_template, request, url_for, jsonify
from application.model.entity.item import Produto
from application.model.entity.price import Price
from application.model.dao.itensDAO import ProdutosDAO

@app.route("/", methods=['GET'])
def home():
    produto_json = open(r'application\controller\json\data.json', 'r')
    produto_json = json.load(produto_json)
    produtosDAO = ProdutosDAO(produto_json)
    produtos_list = produtosDAO.retornar_produto_lista()
    return render_template("index.html", produtos_list=produtos_list)


@app.route("/inserir", methods=['POST'])
def inserir():
    produtosDAO = ProdutosDAO(produto_json)
    produtos_list = produtosDAO.retornar_produto_lista()

    titulo = request.form.get('titulo', None)
    link = request.form.get('link', None)
    descricao = request.form.get('descricao', None)
    tags = request.form.get('tags', None).split(" ")
    id = len(tools_list) + 1
    tools = Tools(id, titulo, link, descricao, tags)
    tools_list.append(tools)
    return render_template("index.html", tools_list=tools_list)


@app.route("/excluir/<int:id>", methods=['GET'])
def excluir(id: int):
    produtosDAO = ProdutosDAO(produto_json)
    produtos_list = produtosDAO.retornar_produto_lista()
    for tools in tools_list:
        if tools.id == id:
            tools_list.remove(tools)
            return render_template("index.html", tools_list=tools_list)
    return render_template("index.html", tools_list=tools_list), 404


@app.route("/busca")
def busca():
    produtosDAO = ProdutosDAO(produto_json)
    produtos_list = produtosDAO.retornar_produto_lista()
    tools_list_filtrado = []
    palavra_chave = request.args.get('palavra_chave')
    pesquisa_tag = request.args.get("in_tags")
    for tools in tools_list:
        if pesquisa_tag != "on":
            if palavra_chave in tools.titulo or palavra_chave in tools.descricao or palavra_chave in tools.tags:
                tools_list_filtrado.append(tools)
        else:
            if palavra_chave in tools.tags:
                tools_list_filtrado.append(tools)

    return render_template("index.html", tools_list=tools_list_filtrado)
