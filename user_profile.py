from flask import Blueprint,render_template,redirect,request,jsonify
from start import get_db

profile_bp = Blueprint(__name__,"profile")
@profile_bp.route("/profile/<username>",methods=['GET','POST'])
def show_user_profile(username):
    if request.method == "POST":
        data = request.get_json()
        operation = data.get("operation")
        if operation == 'change_type':
            changed_type = data.get("changed_type")
            if changed_type == "Private":
                is_private = "True"
            else:
                is_private = 'False'
            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute("update users set is_private=? where username=?",(is_private,username))
                conn.commit()
            return jsonify({
                "changed_type": changed_type
            })
        elif operation == 'name_change':
            data = request.get_json()
            changed_name = data.get("changed_name")

            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute("update users set name=? where username=?",(changed_name,username))
                conn.commit()
                return jsonify({"changed_name": changed_name})
    else:
        with get_db() as conn:
            cursor = conn.cursor()
            name = cursor.execute("select name from users where username=?",(username,)).fetchone()[0]
            is_private = cursor.execute("select is_private from users where username=?",(username,)).fetchone()[0]
            if is_private == 'True':
                first_option = 'Private'
                second_option = 'Public'
            else:
                first_option = 'Public'
                second_option= 'Private'
        return render_template("profile.html",username=username,name=name,first_option=first_option,second_option=second_option)