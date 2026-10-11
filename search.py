from flask import Blueprint,render_template,redirect,request

import sqlite3

search_bp =Blueprint(__name__,"search")

@search_bp.route("/search/<username>")
def search_for_user(username):
    return render_template("search.html",username=username)

@search_bp.route("/fetch_users/<text>",methods=['GET','POST'])
def fetch_users(text):
    query = f"%{text}%"
    