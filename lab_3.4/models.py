from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auditories.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contact(db.Model):

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    auditory = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(100), nullable=True)
    date = db.Column(db.String(25), nullable=True, unique=False)
    time = db.Column(db.String(40), nullable=True, unique=False)

    def __repr__(self):
        return '<Contacts %r>' % self.auditory
