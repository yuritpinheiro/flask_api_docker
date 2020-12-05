from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config.from_object(__name__)
# port = int(os.getenv('PORT', 8080))
port = 8080

@app.route("/", methods=['GET'])
def hello():
    res_body = { "message": "Hello, World!" }
    return jsonify(res_body), 200

@app.route("/echo", methods=['post'])
def echo():
    res = request.get_json()
    return jsonify(res), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)