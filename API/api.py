import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/<string:name>', methods=['GET'])
def helloName(name):
    return "Hello " + name + "!" 

app.run()