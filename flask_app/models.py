from flask_app import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)


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
