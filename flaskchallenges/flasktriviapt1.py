#!/usr/bin/python3
"""Alta3 Research
Simple flask application using redirect()"""

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

pic_location= "https://static.alta3.com/courses/api/lec_flaskcontrol_python/dont-panic.png"

@app.route("/")
def index():
    return render_template("flasktriviapt1.html", pic= pic_location)

@app.route("/login", methods=["POST"])
def login():
    answer = request.form.get("answer")
    if answer == "42":
        return redirect("/correct")
    else:
        return redirect("/")

@app.route("/correct")
def correct():
    return "Correct! The answer was 42."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
