#! -*- conding: utf-8 -*-
from flask import render_template, render_template_string
from flask_menu import register_menu
from . import websys


@websys.route('/web')
@register_menu(websys, '.web', 'Web', order=1)
def web():
    return render_template('web/web.html')
