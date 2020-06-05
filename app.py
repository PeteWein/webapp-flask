import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/home', methods=['GET'])
def home():
    return flask.render_template('hello_world.html') 

app.run()