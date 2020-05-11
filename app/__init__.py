from flask import Flask
# from flask.ext.bootstrap import Bootstrap

from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object('config')
    # app.config['SECRET_KEY'] = os.urandom(24)
    register_blueprint(app)
    bootstrap.init_app(app)
    # bootstrap = Bootstrap(app)
    return app


# def bootstrap_app(app):
#     bootstrap = Bootstrap(app)
#     return bootstrap


def register_blueprint(app):
    # register all the blue_print here
    from app.web.user import user_info
    from app.web.index import index
    app.register_blueprint(user_info)
    app.register_blueprint(index)
