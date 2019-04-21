from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

 # Registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# setting config
from .requests import configure_request
configure_request(app)

return app