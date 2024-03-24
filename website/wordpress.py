"""
wordpress quiz
"""

from flask import Blueprint, render_template, flash, url_for, request, redirect, session
from flask_login import login_required

wordpress = Blueprint("wordpress", __name__)

questions = [
    {
        "question": "What is WordPress?",
        "options": ["A content management system", "A programming language", "A web hosting service", "A database management system"],
        "correct_answer": "A content management system"
    },
    {
        "question": "Which of the following is not a component of WordPress?",
        "options": ["Themes", "Plugins", "Widgets", "Templates"],
        "correct_answer": "Templates"
    },
    {
        "question": "What is a theme in WordPress?",
        "options": ["A design template for a website", "A programming language", "A database table", "A file format for images"],
        "correct_answer": "A design template for a website"
    },
    {
        "question": "Which programming language is used to develop WordPress?",
        "options": ["PHP", "Python", "JavaScript", "Ruby"],
        "correct_answer": "PHP"
    },
    {
        "question": "What is a plugin in WordPress?",
        "options": ["A software extension that adds functionality to WordPress", "A database table", "A file format for images", "A design template for a website"],
        "correct_answer": "A software extension that adds functionality to WordPress"
    },
    {
        "question": "Which of the following is not a type of WordPress plugin?",
        "options": ["Social media sharing", "Search engine optimization", "Image editing", "Security"],
        "correct_answer": "Image editing"
    },
    {
        "question": "What is the WordPress dashboard?",
        "options": ["The administrative area of a WordPress website", "A database management tool", "A file storage location", "A programming interface"],
        "correct_answer": "The administrative area of a WordPress website"
    },
    {
        "question": "Which file is responsible for the overall styling of a WordPress website?",
        "options": ["style.css", "index.php", "functions.php", "header.php"],
        "correct_answer": "style.css"
    },
    {
        "question": "What is a shortcode in WordPress?",
        "options": ["A small piece of code that performs a specific function", "A file storage location", "A database table", "A design template for a website"],
        "correct_answer": "A small piece of code that performs a specific function"
    },
    {
        "question": "What is the purpose of the 'wp-config.php' file in WordPress?",
        "options": ["To store database configuration settings", "To manage website content", "To control plugin settings", "To define the website's structure"],
        "correct_answer": "To store database configuration settings"
    },
    {
        "question": "What is the default database used by WordPress?",
        "options": ["MySQL", "SQLite", "PostgreSQL", "Oracle"],
        "correct_answer": "MySQL"
    },
    {
        "question": "What is a widget in WordPress?",
        "options": ["A small block of content or functionality", "A programming language", "A file format for images", "A design template for a website"],
        "correct_answer": "A small block of content or functionality"
    },
    {
        "question": "What is the purpose of the 'functions.php' file in WordPress?",
        "options": ["To add custom functionality to a theme", "To manage website content", "To control plugin settings", "To define the website's structure"],
        "correct_answer": "To add custom functionality to a theme"
    },
    {
        "question": "What is a permalink in WordPress?",
        "options": ["A permanent URL structure for posts and pages", "A file storage location", "A database table", "A design template for a website"],
        "correct_answer": "A permanent URL structure for posts and pages"
    },
    {
        "question": "Which of the following is not a WordPress user role?",
        "options": ["Administrator", "Editor", "Subscriber", "Developer"],
        "correct_answer": "Developer"
    },
    {
        "question": "What is the purpose of the 'index.php' file in WordPress?",
        "options": ["To serve as the main entry point for a WordPress website", "To manage website content", "To control plugin settings", "To define the website's structure"],
        "correct_answer": "To serve as the main entry point for a WordPress website"
    },
    {
        "question": "What is the purpose of the 'header.php' file in WordPress?",
        "options": ["To define the header section of a theme", "To manage website content", "To control plugin settings", "To define the website's structure"],
        "correct_answer": "To define the header section of a theme"
    },
    {
        "question": "What is the purpose of the 'footer.php' file in WordPress?",
        "options": ["To define the footer section of a theme", "To manage website content", "To control plugin settings", "To define the website's structure"],
        "correct_answer": "To define the footer section of a theme"
    },
    {
        "question": "Which of the following is not a recommended practice for WordPress security?",
        "options": ["Using strong passwords", "Regularly updating themes and plugins", "Using outdated versions of WordPress", "Installing a security plugin"],
        "correct_answer": "Using outdated versions of WordPress"
    },
    {
        "question": "What is the purpose of the 'functions.php' file in a child theme?",
        "options": ["To override or extend the functionality of the parent theme", "To manage website content", "To control plugin settings", "To define the website's structure"],
        "correct_answer": "To override or extend the functionality of the parent theme"
    }
]

course = "WordPress"

@wordpress.route('quiz/quizzes/wordpress', methods=["GET", "POST"])
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
            return redirect(url_for("wordpress.show_score"))

        return render_template("quizzes/python.html", question=questions[question_index], question_index=question_index, score=session["score"], course=course)

    session["score"] = 0
    return render_template("quizzes/python.html", question=questions[0], question_index=0, score=session["score"], course=course)


@wordpress.route("/score")
@login_required
def show_score():
    score = session.pop("score", 0)
    return render_template('quizzes/score.html', score=score)
