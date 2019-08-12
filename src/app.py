from flask import Flask

from .config import app_config

from .models import db

from .views.peopleView import people_api as people_blueprint


def create_app(env_name):
    """
    Create app
    """

    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    db.init_app(app)

    app.register_blueprint(people_blueprint, url_prefix='/api/peoples')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your first endpoint is workin'

    return app
