from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Hola mundo"

from clients import data

@app.route("/players")
def getPlayers():
    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True, port=3000)
