# -*- coding: utf-8 -*-
from flask import Blueprint
websys = Blueprint('web', __name__, template_folder='templates')

from . import routes
