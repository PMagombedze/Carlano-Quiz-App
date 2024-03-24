"""
pyth quiz
"""

from flask import Blueprint, render_template, flash, url_for, request, redirect, session
from flask_login import login_required

pyth = Blueprint("pyth", __name__)

questions = [
    {
        "question": "What is the output of the following code?\n\nx = 5\ny = x + 3\nprint(y)",
        "options": ["5", "3", "8", "Error"],
        "correct_answer": "8"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["String", "Tuple", "List", "Set"],
        "correct_answer": "List"
    },
    {
        "question": "What is the result of the expression 'Hello' + 'World'?",
        "options": ["HelloWorld", "Hello World", "Hello + World", "Error"],
        "correct_answer": "HelloWorld"
    },
    {
        "question": "Which loop is used to iterate over a sequence of elements in Python?",
        "options": ["if-else loop", "for loop", "while loop", "do-while loop"],
        "correct_answer": "for loop"
    },
    {
        "question": "What is the purpose of the 'pass' statement in Python?",
        "options": ["To terminate a loop", "To skip an iteration", "To define an empty code block", "To raise an exception"],
        "correct_answer": "To define an empty code block"
    },
    {
        "question": "What is the output of the following code?\n\nnumbers = [1, 2, 3, 4, 5]\nprint(numbers[1:4])",
        "options": ["[1, 2, 3, 4]", "[2, 3, 4]", "[2, 3]", "[1, 2, 3]"],
        "correct_answer": "[2, 3, 4]"
    },
    {
        "question": "Which of the following is not a valid method for removing an item from a list in Python?",
        "options": ["remove()", "pop()", "delete()", "clear()"],
        "correct_answer": "delete()"
    },
    {
        "question": "What is the output of the following code?\n\nx = 10\ny = 5\nprint(x > y)",
        "options": ["True", "False", "Error", "None"],
        "correct_answer": "True"
    },
    {
        "question": "Which of the following is a built-in module in Python for working with dates and times?",
        "options": ["datetime", "math", "os", "random"],
        "correct_answer": "datetime"
    },
    {
        "question": "What is the result of the expression '10' + 1?",
        "options": ["11", "10", "9", "Error"],
        "correct_answer": "Error"
    },
    {
        "question": "What is the output of the following code?\n\nx = 'Hello'\nprint(x[1:4])",
        "options": ["ell", "H", "Hel", "Hello"],
        "correct_answer": "ell"
    },
    {
        "question": "Which of the following is a Python data type that represents a collection of unique elements?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "correct_answer": "Set"
    },
    {
        "question": "What is the result of the expression 2 ** 3?",
        "options": ["2", "3", "8", "6"],
        "correct_answer": "8"
    },
    {
        "question": "Which keyword is used to exit a loop prematurely in Python?",
        "options": ["break", "exit", "continue", "return"],
        "correct_answer": "break"
    },
    {
        "question": "What is the purpose of the 'continue' statement in Python?",
        "options": ["To terminate a loop", "To skip an iteration", "To resume the next iteration", "To raise an exception"],
        "correct_answer": "To skip an iteration"
    },
    {
        "question": "What is the output of the following code?\n\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "[4, 3, 2, 1]", "[1, 2, 3, [4]]"],
        "correct_answer": "[1, 2, 3, 4]"
    },
    {
        "question": "Which of the following is used to remove leading and trailing whitespace from a string in Python?",
        "options": ["strip()", "trim()", "clean()", "remove()"],
        "correct_answer": "strip()"
    },
    {
        "question": "What is the output of the following code?\n\nx = 5\ny = 3\nprint(x != y)",
        "options": ["True", "False", "Error", "None"],
        "correct_answer": "True"
    },
    {
        "question": "Which module in Python can be used to generate random numbers?",
        "options": ["random", "math", "statistics", "decimal"],
        "correct_answer": "random"
    },
    {
        "question": "What is the result of the expression '10' * 3?",
        "options": ["10", "30", "100", "Error"],
        "correct_answer": "101010"
    }
]

course = "Python"

@pyth.route('quiz/quizzes/python', methods=["GET", "POST"])
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
            return redirect(url_for("pyth.show_score"))

        return render_template("quizzes/python.html", question=questions[question_index], question_index=question_index, score=session["score"], course=course)

    session["score"] = 0
    return render_template("quizzes/python.html", question=questions[0], question_index=0, score=session["score"], course=course)


@pyth.route("/score")
@login_required
def show_score():
    score = session.pop("score", 0)
    return render_template('quizzes/score.html', score=score)
