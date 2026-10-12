from flask import Blueprint,render_template,redirect,request,jsonify

import sqlite3

search_bp =Blueprint(__name__,"search")

@search_bp.route("/search/<username>")
def search_for_user(username):
    return render_template("search.html",username=username)

@search_bp.route("/fetch_users/<text>",methods=['GET','POST'])
def fetch_users(text):
    text,username = text.split("-")
    print(type(username))
    query = f"%{text}%"
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        users = cursor.execute("select username,name from users where username like ?",(query,)).fetchall()
        names = [i[1] for i in users]
        users = [i[0] for i in users]
        statuses = []
        for i in users:
            status = cursor.execute("select status from requests where (requested_by=? and requested_to=?) or (requested_to=? and requested_by=?)",(username,i,username,i)).fetchone()
            if status:
                statuses.append(status)
            else:
                statuses.append("not_requested")
            
        return jsonify({"users": users,
                        "names": names,
                        "statuses": statuses})
