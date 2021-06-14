from flask import Flask, render_template, request, url_for
import os
from application.model.entity.item import Produto

app = Flask(__name__, template_folder=os.path.abspath('application/view/templates'), static_folder=os.path.abspath('application/view/static'))

from application.controller import controller_itens