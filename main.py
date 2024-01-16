import json
from flask import Flask


app = Flask(__name__)


@app.route('/books', methods=['GET'])
def index():
    return json.dumps([
        {
            'title': 'padurea spanzuratilor',
            'autor': 'liviu rebreanu'
        }
    ])



@app.route('/books/<id>', methods=['GET'])
def index2(id):
    return json.dumps([
        {
            'title': 'padurea spanzuratilor',
            'autor': 'liviu rebreanu'
        }
    ])



@app.route('/books', methods=['POST'])
def index3():
    return json.dumps([
        {
            'title': 'padurea spanzuratilor',
            'autor': 'liviu rebreanu'
        }
    ])



@app.route('/books/<id>', methods=['PUT'])
def index4(id):
    return json.dumps([
        {
            'title': 'padurea spanzuratilor',
            'autor': 'liviu rebreanu'
        }
    ])



@app.route('/books/<id>', methods=['DELETE'])
def index5(id):
    return json.dumps([
        {
            'title': 'padurea spanzuratilor',
            'autor': 'liviu rebreanu'
        }
    ])

app.run()