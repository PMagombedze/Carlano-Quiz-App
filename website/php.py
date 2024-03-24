"""
php quiz
"""

from flask import Blueprint, render_template, flash, url_for, request, redirect, session
from flask_login import login_required

php = Blueprint("php", __name__)

questions = [
    {
        "question": "What does PHP stand for?",
        "options": ["Personal Home Page", "PHP: Hypertext Preprocessor", "Programming Hypertext Processor", "Pretextual Hypertext Parser"],
        "correct_answer": "PHP: Hypertext Preprocessor"
    },
    {
        "question": "Which of the following is not a valid way to start a PHP tag?",
        "options": ["<?php", "<?", "<%", "<script>"],
        "correct_answer": "<script>"
    },
    {
        "question": "Which of the following is used to output text in PHP?",
        "options": ["echo", "print", "printf", "display"],
        "correct_answer": "echo"
    },
    {
        "question": "What is the correct way to define a variable in PHP?",
        "options": ["$variable = 5;", "variable = 5;", "var variable = 5;", "set variable = 5;"],
        "correct_answer": "$variable = 5;"
    },
    {
        "question": "What is the concatenation operator in PHP?",
        "options": [".", "+", ",", ":"],
        "correct_answer": "."
    },
    {
        "question": "Which of the following is the correct way to comment a single line in PHP?",
        "options": ["// This is a comment", "# This is a comment", "/* This is a comment */", "<!-- This is a comment -->"],
        "correct_answer": "// This is a comment"
    },
    {
        "question": "Which of the following is used to check if a variable is empty in PHP?",
        "options": ["empty()", "null()", "isset()", "isEmpty()"],
        "correct_answer": "empty()"
    },
    {
        "question": "What is the correct way to include the contents of a PHP file into another PHP file?",
        "options": ["include()", "require()", "import()", "load()"],
        "correct_answer": "include()"
    },
    {
        "question": "Which of the following is not a valid PHP data type?",
        "options": ["integer", "boolean", "string", "float"],
        "correct_answer": "boolean"
    },
    {
        "question": "What is the correct way to start a session in PHP?",
        "options": ["session_start()", "start_session()", "session_begin()", "begin_session()"],
        "correct_answer": "session_start()"
    },
    {
        "question": "Which of the following is used to redirect the user to a different URL in PHP?",
        "options": ["header()", "redirect()", "location()", "forward()"],
        "correct_answer": "header()"
    },
    {
        "question": "What is the correct way to get the length of a string in PHP?",
        "options": ["strlen()", "length()", "strlength()", "string_length()"],
        "correct_answer": "strlen()"
    },
    {
        "question": "Which of the following is used to perform a MySQL database query in PHP?",
        "options": ["mysqli_query()", "mysql_query()", "pdo_query()", "query()"],
        "correct_answer": "mysqli_query()"
    },
    {
        "question": "What is the correct way to handle errors in PHP?",
        "options": ["try-catch blocks", "if-else statements", "error_reporting() function", "throwing exceptions"],
        "correct_answer": "try-catch blocks"
    },
    {
        "question": "Which of the following is used to loop through an array in PHP?",
        "options": ["foreach", "for", "while", "do-while"],
        "correct_answer": "foreach"
    },
    {
        "question": "What is the correct way to define a constant in PHP?",
        "options": ["define('CONSTANT_NAME', value);", "const CONSTANT_NAME = value;", "constant CONSTANT_NAME = value;", "$CONSTANT_NAME = value;"],
        "correct_answer": "const CONSTANT_NAME = value;"
    },
    {
        "question": "Which of the following is used to sort an array in ascending order in PHP?",
        "options": ["sort()", "asort()", "rsort()", "arsort()"],
        "correct_answer": "sort()"
    },
    {
        "question": "What is the correct way to get the current date and time in PHP?",
        "options": ["date('Y-m-d H:i:s')", "now()", "current_datetime()", "datetime()"],
        "correct_answer": "date('Y-m-d H:i:s')"
    },
    {
        "question": "Which of the following is used to handle file uploads in PHP?",
        "options": ["$_GET", "$_POST","$_FILES", "$_REQUEST"],
        "correct_answer": "$_FILES"
    },
    {
        "question": "What is the correct way to connect to a MySQL database in PHP?",
        "options": ["mysql_connect()", "mysqli_connect()", "pdo_connect()", "connect()"],
        "correct_answer": "mysqli_connect()"
    }
]

course = "Php"

@php.route('quiz/quizzes/php', methods=["GET", "POST"])
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
            return redirect(url_for("php.show_score"))

        return render_template("quizzes/python.html", question=questions[question_index], question_index=question_index, score=session["score"], course=course)

    session["score"] = 0
    return render_template("quizzes/python.html", question=questions[0], question_index=0, score=session["score"], course=course)


@php.route("/score")
@login_required
def show_score():
    score = session.pop("score", 0)
    return render_template('quizzes/score.html', score=score)
