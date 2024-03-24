"""
devops quiz
"""

from flask import Blueprint, render_template, flash, url_for, request, redirect, session
from flask_login import login_required

devops = Blueprint("devops", __name__)

questions = [
    {
        "question": "What is DevOps?",
        "options": ["A software development methodology", "A programming language", "A project management tool", "A culture and set of practices"],
        "correct_answer": "A culture and set of practices"
    },
    {
        "question": "Which of the following is a key objective of DevOps?",
        "options": ["Faster time to market", "Increasing software complexity", "Creating silos between teams", "Slowing down software development"],
        "correct_answer": "Faster time to market"
    },
    {
        "question": "What is the primary goal of continuous integration (CI) in DevOps?",
        "options": ["To automate the process of merging code changes", "To manually test software before release", "To create isolated development environments", "To optimize server configurations"],
        "correct_answer": "To automate the process of merging code changes"
    },
    {
        "question": "What is the primary goal of continuous delivery (CD) in DevOps?",
        "options": ["To automate the deployment of software to production", "To create isolated development environments", "To manually test software before release", "To optimize server configurations"],
        "correct_answer": "To automate the deployment of software to production"
    },
    {
        "question": "What is the purpose of infrastructure as code (IaC) in DevOps?",
        "options": ["To manage and provision infrastructure resources using code", "To track code changes in version control", "To automate the process of merging code changes", "To optimize server configurations"],
        "correct_answer": "To manage and provision infrastructure resources using code"
    },
    {
        "question": "Which of the following is not a commonly used version control system in DevOps?",
        "options": ["Git", "Subversion", "Mercurial", "Docker"],
        "correct_answer": "Docker"
    },
    {
        "question": "What is the purpose of configuration management in DevOps?",
        "options": ["To automate the management of software configurations", "To track code changes in version control", "To create isolated development environments", "To optimize server configurations"],
        "correct_answer": "To automate the management of software configurations"
    },
    {
        "question": "Which of the following is a popular containerization platform used in DevOps?",
        "options": ["Docker", "Kubernetes", "Jenkins", "Ansible"],
        "correct_answer": "Docker"
    },
    {
        "question": "What is the primary goal of continuous monitoring in DevOps?",
        "options": ["To collect and analyze real-time data from software and infrastructure", "To manually test software before release", "To create isolated development environments", "To optimize server configurations"],
        "correct_answer": "To collect and analyze real-time data from software and infrastructure"
    },
    {
        "question": "What is the purpose of automated testing in DevOps?",
        "options": ["To validate the functionality and quality of software", "To track code changes in version control", "To create isolated development environments", "To optimize server configurations"],
        "correct_answer": "To validate the functionality and quality of software"
    },
    {
        "question": "What is the role of collaboration and communication in DevOps?",
        "options": ["To foster a culture of shared responsibility and transparency", "To create isolated development environments", "To manually test software before release", "To optimize server configurations"],
        "correct_answer": "To foster a culture of shared responsibility and transparency"
    },
    {
        "question": "Which of the following is not an essential characteristic of DevOps?",
        "options": ["Agile development", "Continuous integration", "Continuous improvement", "Manual deployment"],
        "correct_answer": "Manual deployment"
    },
    {
        "question": "What is the purpose of incident management in DevOps?",
        "options": ["To respond to and resolve incidents affecting software and infrastructure", "To track code changes in version control", "To create isolated development environments", "To optimize server configurations"],
        "correct_answer": "To respond to and resolve incidents affecting software and infrastructure"
    },
    {
        "question": "What is the role of automation in DevOps?",
        "options": ["To reduce manual effort and improve efficiency", "To manually test software before release", "To create isolated development environments", "To optimize server configurations"],
        "correct_answer": "To reduce manual effort and improve efficiency"
    },
    {
        "question": "Which of the following is a common DevOps tool for continuous integration and delivery?",
        "options": ["Jenkins", "Chef", "Puppet", "Terraform"],
        "correct_answer": "Jenkins"
    },
    {
        "question": "Whatis the purpose of DevOps pipelines?",
        "options": ["To automate the software development lifecycle", "To track code changes in version control", "To create isolated development environments", "To optimize server configurations"],
        "correct_answer": "To automate the software development lifecycle"
    },
    {
        "question": "Which of the following is a key principle of DevOps?",
        "options": ["Collaboration over competition", "Manual processes over automation", "Siloed teams over cross-functional teams", "Waterfall development over agile development"],
        "correct_answer": "Collaboration over competition"
    },
    {
        "question": "What is the purpose of infrastructure monitoring in DevOps?",
        "options": ["To track the performance and availability of infrastructure resources", "To manually test software before release", "To create isolated development environments", "To optimize server configurations"],
        "correct_answer": "To track the performance and availability of infrastructure resources"
    },
    {
        "question": "Which of the following is a popular DevOps practice for managing software releases?",
        "options": ["Blue-green deployment", "Waterfall development", "Functional programming", "Extreme programming"],
        "correct_answer": "Blue-green deployment"
    },
    {
        "question": "What is the role of feedback loops in DevOps?",
        "options": ["To gather insights and improve processes", "To track code changes in version control", "To create isolated development environments", "To optimize server configurations"],
        "correct_answer": "To gather insights and improve processes"
    }
]

course = "DevOps"

@devops.route('quiz/quizzes/devops', methods=["GET", "POST"])
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
            return redirect(url_for("devops.show_score"))

        return render_template("quizzes/python.html", question=questions[question_index], question_index=question_index, score=session["score"], course=course)

    session["score"] = 0
    return render_template("quizzes/python.html", question=questions[0], question_index=0, score=session["score"], course=course)


@devops.route("/score")
@login_required
def show_score():
    score = session.pop("score", 0)
    return render_template('quizzes/score.html', score=score)
