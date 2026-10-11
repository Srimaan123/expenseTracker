from flask import Flask,render_template,request,Blueprint
from auth import auth_bp
from main import main_bp
from search import search_bp
from structure import init_db
import sqlite3

app = Flask(__name__)

init_db()

app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(search_bp)

if __name__ == "__main__":
    app.run(debug=True)