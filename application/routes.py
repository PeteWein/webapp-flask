"""Route declaration."""
from flask import current_app as app
from flask import render_template, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin
CORS(app)

#define and populate our routes
@app.route('/')
def root_dir():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html'), 200

# error handling
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('page_not_found.html'), 404

@app.route('/api/favoriteFoods', methods=['GET'])
def favoriteFoods():
    favoriteFoods = ['Pizza', 'Cheesesteaks', 'Bagels']
    return jsonify({"foods": favoriteFoods})

