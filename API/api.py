import flask
import json
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

# Get permit result
# if id is provided, return certain result.
# Otherwise, return all
#  /permit?id= <id>
@app.route('/permit', methods=['GET'])
def getPermit():
    with open('dummy.json','r') as jsonfile:
        permitData = json.loads(jsonfile.read())
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return json.dumps(permitData)
    
    for permit in permitData:
        if permit['id'] == id:
            return jsonify(permit)

if __name__ == '__main__':
    app.run(debug=True)