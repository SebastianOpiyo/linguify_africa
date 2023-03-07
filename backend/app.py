from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create SQLAlchemy instance
db = SQLAlchemy(app)


# MODELS
class Lingua(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    statement = db.Column(db.String(100), nullable=False)
    transalation = db.Column(db.String(100), nullable=False)
    language = db.Column(db.string(50), nullable=False)

    def __repr__(self):
        return f'<User {self.language}>'


# ROUTES

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    statement = request.form['statement']
    translation = request.form['translation']
    language = request.form['language']
    # create a new user object
    lingua = Lingua(statement=statement, translation=translation, language=language)

    # add user object to the database
    db.session.add(lingua)
    db.session.commit()

    return f'Thank you for submitting your information on, {language}!'
if __name__ == '__main__':
    app.run(debug=True)
