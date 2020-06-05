import os, yaml
from flask import Flask, render_template, redirect, url_for

def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)

    # set relative filepath
    dirname = os.path.dirname(__file__)

    # grab yaml for web config
    with open(os.path.join(dirname, 'config/config.yaml')) as f:
        wc_data = yaml.load(f, Loader=yaml.FullLoader)

    # define and populate our routes
    @app.route('/')
    def root_dir():
        return redirect(url_for(wc_data['root']['redirect']))
    
    @app.route('/home', methods=['GET'])
    def home():
        return render_template(wc_data['home']['template'])


    return app