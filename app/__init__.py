from flask import Flask
from pathlib import Path
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


root_dir = Path(__file__).parent.parent
template_dir = root_dir / 'resources/templates'

app = Flask(__name__, template_folder=template_dir, 
                static_url_path='/static', static_folder='../resources/static')
app.config.from_object(Config)

#login = LoginManager(app)
#login.login_view = 'login'
#login.login_message = 'Inicie sesión para acceder a esta página'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.category import categoryRouter, categoryModel
from app.product import productRouter,productModel
from app.carrito import carritoModel,carritoRouter