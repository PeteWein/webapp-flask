import os, yaml
from flask import Flask, render_template, redirect, url_for

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

# error handling
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
