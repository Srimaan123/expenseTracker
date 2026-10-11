from flask import Blueprint,render_template,request,redirect

import sqlite3

auth_bp = Blueprint(__name__,'auth')

@auth_bp.route("/",methods=['GEt','POST'])
def login_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()
            user = cursor.execute("select username,password from users where username=? and password=?",(username,password)).fetchone()
            
        if user:
            return redirect(f"/main/{username}")
        else:
            return "invalid username or password"

    else:
        return render_template("index.html")

@auth_bp.route("/createaccount",methods=['GET','POST'])
def createaccount():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        mobile = request.form.get("mobile")

        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("insert into users(username,password,mobile_number) values(?,?,?)",(username,password,mobile))
            conn.commit()
        
        redirect("/")
    else:
        return render_template("create_account.html")
