from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/usn_management'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)
class USNManagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
class LogTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(20), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': 
        usn = request.form.get('usn')
        user = USNManagement.query.filter_by(usn=usn).first()
        if user:
            log = LogTable(usn=usn)
            db.session.add(log)
            db.session.commit()
            return f"USN {usn} for {user.name} logged successfully."
        else:
            return "USN not found."
    return render_template('index.html')
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
