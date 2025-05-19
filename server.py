# following the tutorial
# https://www.youtube.com/watch?v=7LNl2JlZKHA
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/activities")
def activities():
    return  ["ONE", "TWO", "THREE"]


if __name__ == "__main__":
    app.run(debug=True)
