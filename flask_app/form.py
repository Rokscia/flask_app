from wtforms import SelectMultipleField, TextAreaField
from flask_app.models import Author
from wtforms_alchemy import ModelForm
from flask_app.models import Post


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

