# -*- coding: utf-8 -*-
from flask import Blueprint
basesys = Blueprint('base', __name__, template_folder='templates')

from . import routes
