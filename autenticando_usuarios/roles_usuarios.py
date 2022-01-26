# -*- coding: utf-8 -*-
import os
import csv
import re
from flask import Flask, render_template, request, redirect, url_for
from flask_login import (
    current_user, login_user, logout_user,
    login_required, LoginManager, UserMixin
)
from peewee import *


app = Flask(__name__)
app.secret_key = b'Zlnkkmv37di0aV3f'
login_manager = LoginManager()
login_manager.init_app(app)

#--------- SISTEMA ---------#

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.get_or_none(Users.username == username)
        if user != None and user.password == password:
            login_user(user, user.email)
            return redirect(url_for('system'))
    
    return render_template('login.html')

@app.route('/system')
@login_required
def system():
    return render_template('system.html')

@app.get('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


#--------- BASE DE DATOS ---------#

db = PostgresqlDatabase('roles_db', user='mibase', password='mibase',
    host='localhost', port=5432, autorollback=True)

class BaseModel(Model):
    class Meta:
        database = db

class Users(UserMixin, BaseModel):
    id = AutoField()
    username = CharField(max_length=1024)
    password = CharField(max_length=1024)
    email = CharField(max_length=1024)
    
    @login_manager.user_loader
    def load_user(user_id):
        for user in Users:
            if user.id == int(user_id):
                return user
        return None

db.create_tables([Users], safe=True)

def load_data():
    path_data_file = os.path.join('data', 'users.csv')
    data = []
    with open(path_data_file) as csv_file:
        dict_file = csv.DictReader(csv_file, delimiter=';')
        for l in dict_file:
            data.append(dict(l))
    for d in data:
        rec = Users.get_or_none(Users.username == d['username'])
        if rec == None:
            Users.create(**d)

load_data()

#--------- Arranque del sistema ---------#
app.run(host='0.0.0.0', port='8080', debug=True)
