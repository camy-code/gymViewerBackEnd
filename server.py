# following the tutorial
    # https://www.youtube.com/watch?v=7LNl2JlZKHA
from flask import Flask

app = Flask(__name__)

@app.route("/members")
def members():
    return {"members":["ONE","TWO","THREE"]}


if __name__ == "__main__":
    app.run(debug=True)
