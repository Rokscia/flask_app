from constants.posts import POSTS
from flask_app.models import Post, app, db


app.app_context().push()
#
# all_messages = Post.query.all()
#
# print(all_messages)


def insert_posts_to_db():
    for post in POSTS:
        db.session.add(Post(post['data'], post['autorius'], post['pavadinimas'], post['tekstas']))


insert_posts_to_db()
db.session.commit()
