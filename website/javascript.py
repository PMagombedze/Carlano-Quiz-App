"""
javascript quiz
"""

from flask import Blueprint, render_template, flash, url_for, request, redirect, session
from flask_login import login_required

javascript = Blueprint("javascript", __name__)

questions = [
    {
        "question": "What is JavaScript?",
        "options": ["A programming language", "A markup language", "A database management system", "A web browser"],
        "correct_answer": "A programming language"
    },
    {
        "question": "Which of the following is not a JavaScript data type?",
        "options": ["String", "Boolean", "Number", "Array"],
        "correct_answer": "Array"
    },
    {
        "question": "How do you declare a variable in JavaScript?",
        "options": ["var", "let", "const", "All of the above"],
        "correct_answer": "All of the above"
    },
    {
        "question": "What is the output of the following code?\n\nconsole.log(2 + '2');",
        "options": ["4", "22", "Error", "NaN"],
        "correct_answer": "22"
    },
    {
        "question": "Which operator is used for concatenating strings in JavaScript?",
        "options": ["+", "-", "*", "/"],
        "correct_answer": "+"
    },
    {
        "question": "What is the purpose of the 'if' statement in JavaScript?",
        "options": ["To declare a function", "To iterate over a loop", "To make a decision based on a condition", "To import external libraries"],
        "correct_answer": "To make a decision based on a condition"
    },
    {
        "question": "Which method is used to add an element to the end of an array in JavaScript?",
        "options": ["push()", "pop()", "shift()", "unshift()"],
        "correct_answer": "push()"
    },
    {
        "question": "What is the result of the expression '5' == 5?",
        "options": ["true", "false", "Error", "NaN"],
        "correct_answer": "true"
    },
    {
        "question": "Which function is used to parse a string to an integer in JavaScript?",
        "options": ["parseInt()", "parseFloat()", "toString()", "toFixed()"],
        "correct_answer": "parseInt()"
    },
    {
        "question": "What is the output of the following code?\n\nconsole.log(typeof null);",
        "options": ["null", "object", "undefined", "Error"],
        "correct_answer": "object"
    },
    {
        "question": "Which loop is used to iterate over the elements of an array in JavaScript?",
        "options": ["if-else loop", "for loop", "while loop", "do-while loop"],
        "correct_answer": "for loop"
    },
    {
        "question": "What is the purpose of the 'return' statement in a function?",
        "options": ["To terminate the function", "To skip the current iteration", "To pass a value back to the caller", "To raise an exception"],
        "correct_answer": "To pass a value back to the caller"
    },
    {
        "question": "Which method is used to remove the last element from an array in JavaScript?",
        "options": ["push()", "pop()", "shift()", "unshift()"],
        "correct_answer": "pop()"
    },
    {
        "question": "What is the output of the following code?\n\nconsole.log(10 > 5 && 5 < 3);",
        "options": ["true", "false", "Error", "NaN"],
        "correct_answer": "false"
    },
    {
        "question": "Which function is used to find the length of a string in JavaScript?",
        "options": ["length()", "size()", "count()", "charAt()"],
        "correct_answer": "length()"
    },
    {
        "question": "What is the result of the expression 'undefined' == undefined?",
        "options": ["true", "false", "Error", "NaN"],
        "correct_answer": "true"
    },
    {
        "question": "Which method is used to convert a string to uppercase in JavaScript?",
        "options": ["toUpperCase()", "toLowerCase()", "trim()", "substring()"],
        "correct_answer": "toUpperCase()"
    },
    {
        "question": "What is the output of the following code?\n\nconsole.log(3 + 2 + '7');",
        "options": ["12", "57", "Error", "NaN"],
        "correct_answer": "57"
    },
    {
        "question": "Which keyword is used to define a function in JavaScript?",
        "options": ["def", "function", "define", "fun"],
        "correct_answer": "function"
    },
    {
        "question": "What is the output of the following code?\n\nconsole.log(typeof null);",
        "options": ["null", "object", "undefined", "Error"],
        "correct_answer": "object"
    }
]

course = "JavaScript"

@javascript.route('quiz/quizzes/javascript', methods=["GET", "POST"])
@login_required
def quiz():
    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":
        selected_answer = request.form.get("answer")
        question_index = int(request.form.get("question_index"))

        if selected_answer == questions[question_index]["correct_answer"]:
            session["score"] += 1
            flash("Correct! 🎉")
        else:
            flash("Incorrect")

        question_index += 1

        if question_index >= len(questions):
            return redirect(url_for("javascript.show_score"))

        return render_template("quizzes/python.html", question=questions[question_index], question_index=question_index, score=session["score"], course=course)

    session["score"] = 0
    return render_template("quizzes/python.html", question=questions[0], question_index=0, score=session["score"], course=course)


@javascript.route("/score")
@login_required
def show_score():
    score = session.pop("score", 0)
    return render_template('quizzes/score.html', score=score)
