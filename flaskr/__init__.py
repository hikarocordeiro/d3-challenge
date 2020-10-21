import os

from flask import Flask

def create_app(test_config=None, debug=False):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')
    app.debug = debug

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import covid19
    app.register_blueprint(covid19.bp)
    app.add_url_rule('/', endpoint='index')

    return app