#! -*- conding: utf-8 -*-
from flask import Flask, render_template, render_template_string
from flask_menu import Menu, register_menu

app = Flask(__name__)
Menu(app=app)

@app.route('/')
@register_menu(app, '.index', 'Home', order=0)
def index():
    return render_template('index.html')

@app.route('/first')
@register_menu(app, '.first', 'First', order=10)
def first():
    return render_template('first.html')

@app.route('/second')
@register_menu(app, '.second', 'Second', order=20)
def second():
    return render_template('second.html')

if __name__ == '__main__':
    app.run(debug=True)
