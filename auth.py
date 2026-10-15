from flask import Blueprint,render_template,request,redirect

from start import get_db

auth_bp = Blueprint(__name__,'auth')

@auth_bp.route("/",methods=['GEt','POST'])
def login_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        with get_db() as conn:
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

        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("insert into users(username,password,mobile_number,name,is_private) values(?,?,?,?,?)",(username,password,mobile,username,'False'))
            conn.commit()
        
        return redirect("/")
    else:
        return render_template("create_account.html")
