#! -*- conding: utf-8 -*-
from flask import Flask
from flask_menu import Menu

mi_sistema = Flask(__name__)
Menu(app=mi_sistema)

from apps.base import basesys
from apps.web import websys

mi_sistema.register_blueprint(basesys)
mi_sistema.register_blueprint(websys)
mi_sistema.run(host='0.0.0.0', debug=True)
