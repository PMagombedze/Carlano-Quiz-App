"""
linux quiz
"""

from flask import Blueprint, render_template, flash, url_for, request, redirect, session
from flask_login import login_required

linux = Blueprint("linux", __name__)

questions = [
    {
        "question": "What is Linux?",
        "options": ["An operating system", "A programming language", "A web browser", "A database management system"],
        "correct_answer": "An operating system"
    },
    {
        "question": "Which command is used to list files and directories in Linux?",
        "options": ["ls", "cd", "mv", "rm"],
        "correct_answer": "ls"
    },
    {
        "question": "What does the 'chmod' command do in Linux?",
        "options": ["Change file ownership", "Change file permissions", "Change file extension", "Change file size"],
        "correct_answer": "Change file permissions"
    },
    {
        "question": "Which command is used to create a new directory in Linux?",
        "options": ["mkdir", "rmdir", "cd", "ls"],
        "correct_answer": "mkdir"
    },
    {
        "question": "What is the root directory in Linux?",
        "options": ["/", "/root", "/home", "/var"],
        "correct_answer": "/"
    },
    {
        "question": "Which command is used to copy files and directories in Linux?",
        "options": ["cp", "mv", "rm", "mkdir"],
        "correct_answer": "cp"
    },
    {
        "question": "What does the command 'grep' do in Linux?",
        "options": ["Find and replace text", "Search for files", "List directory contents", "Search for patterns in files"],
        "correct_answer": "Search for patterns in files"
    },
    {
        "question": "Which command is used to display the current working directory in Linux?",
        "options": ["pwd", "ls", "cd", "cat"],
        "correct_answer": "pwd"
    },
    {
        "question": "What does the 'apt-get' command do in Linux?",
        "options": ["Install software packages", "Remove software packages", "Update software packages", "All of the above"],
        "correct_answer": "All of the above"
    },
    {
        "question": "Which command is used to change the current directory in Linux?",
        "options": ["cd", "ls", "mkdir", "pwd"],
        "correct_answer": "cd"
    },
    {
        "question": "What is the purpose of the 'chmod +x' command in Linux?",
        "options": ["Change file ownership", "Change file permissions to executable", "Change file extension", "Change file size"],
        "correct_answer": "Change file permissions to executable"
    },
    {
        "question": "Which command is used to remove files and directories in Linux?",
        "options": ["rm", "mv", "cp", "mkdir"],
        "correct_answer": "rm"
    },
    {
        "question": "What does the 'man' command do in Linux?",
        "options": ["Display the current date and time", "Search for files", "List directory contents", "Display manual pages"],
        "correct_answer": "Display manual pages"
    },
    {
        "question": "Which command is used to rename files and directories in Linux?",
        "options": ["mv", "cp", "rm", "mkdir"],
        "correct_answer": "mv"
    },
    {
        "question": "What is the purpose of the 'chown' command in Linux?",
        "options": ["Change file ownership", "Change file permissions", "Change file extension", "Change file size"],
        "correct_answer": "Change file ownership"
    },
    {
        "question": "Which command is used to compress files and directories in Linux?",
        "options": ["tar", "gzip", "zip", "unzip"],
        "correct_answer": "tar"
    },
    {
        "question": "What does the 'df' command do in Linux?",
        "options": ["Display system information", "Display disk usage", "Display file contents", "Display network configuration"],
        "correct_answer": "Display disk usage"
    },
    {
        "question": "Which command is used to find files and directories in Linux?",
        "options": ["find", "grep", "ls", "cd"],
        "correct_answer": "find"
    },
    {
        "question": "What is the purpose of the 'sudo' command in Linux?",
        "options": ["Switch to the superuser account", "Display system information", "Change file permissions", "List directory contents"],
        "correct_answer": "Switch to the superuser account"
    },
    {
        "question": "Which command is used to edit text files in Linux?",
        "options": ["vi", "ls", "cd", "mkdir"],
        "correct_answer": "vi"
    }
]

course = "Linux"

@linux.route('quiz/quizzes/linux', methods=["GET", "POST"])
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
            return redirect(url_for("linux.show_score"))

        return render_template("quizzes/python.html", question=questions[question_index], question_index=question_index, score=session["score"], course=course)

    session["score"] = 0
    return render_template("quizzes/python.html", question=questions[0], question_index=0, score=session["score"], course=course)


@linux.route("/score")
@login_required
def show_score():
    score = session.pop("score", 0)
    return render_template('quizzes/score.html', score=score)
