from flask import Flask
from flask import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="\xcfJb\xa9\xc10\x8f\xe6\xaf\x8c\xda\xf45\xba\xfb\x97\x83\xe4\r\xdb"
    app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DB_NAME}]'
    app.init_app(app)
    
    from .view import view
    from .auth import auth
    
    
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app