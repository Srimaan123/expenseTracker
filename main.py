from flask import Blueprint,redirect,render_template,request

import sqlite3

main_bp = Blueprint(__name__,"main")

@main_bp.route("/main/<username>")
def show_landing_page(username):
    return render_template("main.html",username=username)

@main_bp.route("/home/<username>")
def home(username):
    return render_template("feed.html",username=username)
