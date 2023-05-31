from flask import Flask, jsonify
import json


app = Flask(__name__)

@app.route("/last_item", methods=['GET'])
def hello_new():
    data_logger = {}
    x = open('data_logger.json')
    data_logger = json.load(x)

    last_val = {}
    last_val = data_logger.popitem()
    data_logger.update({last_val[0]:last_val[1]})

    return jsonify({last_val[0]:last_val[1]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')