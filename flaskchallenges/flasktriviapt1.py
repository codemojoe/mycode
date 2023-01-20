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

incorrect_answers = []
for incorrect_answer in results["incorrect_answers"]:
    incorrect_answers.append(incorrect_answer)

answer = results["correct_answer"]

#username = input("What is your name?\n")

@app.route("/<username>")
def index(username):
    return render_template("flasktriviapt1.html", name = username, pic= pic_location, question = question, answer1 = incorrect_answers[0], answer2 = incorrect_answers[1], answer3 = incorrect_answers[2],  answer = answer)

@app.route("/login", methods=["POST"])
def login():
    user_answer = request.form.get("answer")
    #return redirect("/outcome")
    if user_answer == answer:
        return redirect("/outcome")
    else:
        return redirect("/<username>")

@app.route("/outcome")
def correct():
    return render_template("flasktriviaoutcome.html", pic= pic_location)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
