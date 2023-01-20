#!/usr/bin/python3
"""Alta3 Research
Simple flask application using redirect()"""

from flask import Flask, render_template, url_for, request, redirect
import requests

URL = "https://opentdb.com/api.php?amount=1"

app = Flask(__name__)

pic_location= "https://static.alta3.com/courses/api/lec_flaskcontrol_python/dont-panic.png"

data = requests.get(URL).json()
results = data["results"][0]
question = results["question"]
answer = results["correct_answer"]

@app.route("/<username>")
def index(username):
    return render_template("flasktriviapt1.html", name = username, pic= pic_location, question = question, answer = answer)

@app.route("/login", methods=["POST"])
def login():
    user_answer = request.form.get("answer")
    redirect("/outcome/<username>")
    #if user_answer == answer:
        #return redirect("/correct")
    #else:
        #return redirect("/<username>")

@app.route("/outcome/<username>")
def correct(username):
    return render_template("flasktriviaoutcome.html", name = username, pic= pic_location)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
