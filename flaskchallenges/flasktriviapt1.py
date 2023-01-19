#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

def main():

    @app.route("/")
    def trivia_form():
        return render_template("flasktriviapt1.html", name = username)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
    main()
