#! -*- conding: utf-8 -*-
from flask import render_template, render_template_string
from flask_menu import register_menu
from . import basesys


@basesys.route('/')
@register_menu(basesys, '.index', 'Home', order=0)
def index():
    return render_template('base/index.html')
