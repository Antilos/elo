import os

from flask import Flask, render_template
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     SQLALCHEMY_DATABASE_URI=os.path.join(app.instance_path, 'app.sqlite'),
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # app.config.from_pyfile('config.py', silent=True)
        app.config.from_object(Config)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register with extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    #index page
    @app.route('/')
    @app.route('/index')
    @app.route('/home')
    def index():
        return render_template("index.html", title="Home Page")

    #register blueprints
    from .routes import game, users
    app.register_blueprint(game.bp)
    app.register_blueprint(users.bp)

    return app