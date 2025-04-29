from flask import Blueprint, render_template, request, redirect, url_for
from app.controllers.user_controller import create_user
from service.db import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    return render_template('form.html')

@user_bp.route('/register', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    senha = request.form['senha']
    x = request.form['x']
    instagram = request.form['instagram']
    gostos = request.form.getlist('gostos')

    create_user(nome, cpf, email, senha, x, instagram, gostos)
    flash('Usuário cadastrado com sucesso!', 'success')
    return redirect(url_for('user.index'))