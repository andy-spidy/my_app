import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# create some test data
cars = [
    {'id': 0,
     'car': 'Skoda Octavia',
     'owner': 'John Travolta',
     'color': 'grey',
     'year': '2012'},
    {'id': 1,
     'car': 'Porsche 911',
     'owner': 'James Bond',
     'color': 'light red',
     'year': '1978'},
    {'id': 2,
     'car': 'Hadraplan',
     'owner': 'Vrchni prchni',
     'color': 'yellow',
     'year': '1964'}
]


@app.route('/', methods=['GET'])
# example: 127.0.0.1
def home():
    return '''<h1>Cars database</h1>
<p>A prototype API - demo purpose</p>'''


@app.route('/api/v1/resources/cars/all', methods=['GET'])
# example: 127.0.0.1/api/v1/resources/cars/all
def api_all():
    return jsonify(cars)


@app.route('/api/v1/resources/cars', methods=['GET'])
# example: 127.0.0.1/api/v1/resources/cars?id=0
def api_id():
    # check if an ID was provided as part of the URL
    # if ID is provided, assign it to a variable
    # if no ID is provided, display an error in the browser
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field defined, please specify an id."

    # create an empty list for results
    results = []

    # loop through the data and match results that fit the requested ID
    # IDs are unique, but other fields might return many results
    for car in cars:
        if car['id'] == id:
            results.append(car)

    # use the jsonify function from Flask to convert our list of
    # python dictionaries to the JSON format.
    return jsonify(results)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=7000)

# app.run()

