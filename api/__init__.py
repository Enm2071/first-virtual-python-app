from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://eoldjcyi:rqGby9iM7U1hu6D_fRTlb7htlW55g95F@salt.db.elephantsql.com/eoldjcyi"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'My First API !!'

if __name__ == "__main__":
    app.run(debug=True)

