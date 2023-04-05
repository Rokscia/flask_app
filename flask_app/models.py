from flask_app import app, db, bcrypt, login_manager
from flask_migrate import Migrate
from flask_login import UserMixin
from datetime import datetime


migrate = Migrate(app, db)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('Username', db.String(20), unique=True, nullable=False)
    email = db.Column('Email', db.String(100), unique=True, nullable=False)
    password = db.Column('Password', db.String, nullable=False)
    created_on = db.Column('Created on', db.DateTime, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()

    def __repr__(self):
        return f'User: {self.username}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


helper_table = db.Table('helper',
                        db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                        db.Column('author_id', db.Integer, db.ForeignKey('author.id')))


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    title = db.Column(db.String(80))
    text = db.Column(db.Text)
    # author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    authors = db.relationship('Author', secondary=helper_table, backref='posts')

    # def __init__(self, date, title, text, author_id):
    def __init__(self, date, title, text):
        self.date = date
        self.title = title
        self.text = text
        # self.author_id = author_id

    def __repr__(self):
        # return f'{self.date} - {self.author_id} - {self.title}'
        return f'{self.date} - {self.title}'


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    nationality = db.Column(db.String(40))
    phone = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100), unique=True)
    # posts = db.relationship('Post', backref='author')

    def __init__(self, name, nationality, phone, email):
        self.name = name
        self.nationality = nationality
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"{self.name.split()[0][0].upper()}. {' '.join(self.name.split()[1:])} ({self.nationality})"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nationality': self.nationality,
            'phone': self.phone,
            'email': self.email
        }
