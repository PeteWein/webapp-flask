import os, yaml
from flask import Flask, render_template
#from src import app

def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)

    # set relative filepath
    dirname = os.path.dirname(__file__)

    # grab yaml for web config
    with open(os.path.join(dirname, 'config/config.yaml')) as f:
        wc_data = yaml.load(f, Loader=yaml.FullLoader)

    @app.route('/home', methods=['GET'])
    def home():
        return render_template(wc_data['home']['template'])


    return app