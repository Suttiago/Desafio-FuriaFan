from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.routes.user_routes import user_bp
from app.service.db import db
app = Flask(__name__,
            template_folder="app/templates")
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
