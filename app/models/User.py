from service import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha = db.Column(db.String(120), nullable=False)
    x = db.Column(db.String(200))
    instagram = db.Column(db.String(200))
    gostos = db.Column(db.Text)
    
    def __init__(self,nome,cpf,email,senha,x,instagram,gostos):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.x = x
        self.instagram = instagram
        self.gostos = gostos
           
