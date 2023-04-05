from wtforms import SelectMultipleField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from flask_app.models import Author
from wtforms_alchemy import ModelForm
from flask_app.models import Post
from flask_wtf import FlaskForm
import app


class RegisterForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    email = StringField('Email address', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    confirm_password = PasswordField('Confirm Password', [EqualTo('password', 'Passwords do not match')])
    submit = SubmitField('Register')

    def check_username(self, username):
        user = app.User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already registered')

    def check_email(self, email):
        user = app.User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already registered')


class LoginForm(FlaskForm):
    email = StringField('Email address', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField('Login')


class PostForm(ModelForm):
    authors = SelectMultipleField('Author', coerce=int)

    class Meta:
        model = Post

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.authors.choices = [(author.id, author.name) for author in Author.query.all()]


# class PostForm(FlaskForm):
#     date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
#     title = StringField('Title', validators=[DataRequired()])
#     text = TextAreaField('Text', validators=[DataRequired()])
#     author_id = SelectField('Author', coerce=int)
#
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.author_id.choices = [(author.id, author.name) for author in Author.query.all()]

