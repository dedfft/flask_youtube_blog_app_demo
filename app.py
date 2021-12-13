from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager





app = Flask(__name__)
app.config['SECRET_KEY'] = "helloweeef"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


from views import views
from auth import auth
app.register_blueprint(views)
app.register_blueprint(auth)


db = SQLAlchemy()
DB_NAME = 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
from models import User



db.init_app(app)
def create_db():
    if not path.exists(DB_NAME):
        db.create_all(app=app)

create_db()


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))



if __name__ == '__main__':
    app.run()
