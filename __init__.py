import os

from flask import Flask


def create_app(test_config=None):
    # constants
    SECRET_KEY = 'dev'
    DB_NAME = 'learning'

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        DATABASE=os.path.join(app.instance_path, DB_NAME + '.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says Salam
    @app.route('/salam')
    def hello():
        return 'Salam, World!'

    return app