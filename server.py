# following the tutorial
# https://www.youtube.com/watch?v=7LNl2JlZKHA
from flask import Flask
from flask_cors import CORS

# Imports to code that I write
import scraper as sc

app = Flask(__name__)
CORS(app)


@app.route("/activities")
def activities():
    # return  sc.dum_scrape()
    return sc.realScrape()


if __name__ == "__main__":
    app.run(debug=True)
