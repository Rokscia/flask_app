from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_app import app, db
from .form import PostForm, RegisterForm, LoginForm
from .models import Post, Author, User
from werkzeug.datastructures import MultiDict


@app.route("/")
def home():
    return render_template('home.html')


@app.context_processor
def inject_forms():
    return dict(login_form=LoginForm(), register_form=RegisterForm())


@app.route("/register", methods=['POST'])
def register():
    # db.create_all()
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('New user was successfully registered. You can log in now', 'success')
        return redirect(url_for('home'))
    return jsonify({'success': False, 'errors': form.errors})


# @app.route("/login", methods=['POST'])
# def login():
#     pass
@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('greetings.html', username=username)
    else:
        return render_template('login.html')



def check_if_leap_year(year: int):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f' The year {year} is LEAP year!'
    return f' The year {year} is NOT a LEAP year!'


@app.route("/leapyear", methods=['GET', 'POST'])
def leap_year():
    leap_years = [year for year in range(1904, 2100, 4)]
    if request.method == 'POST':
        year = request.form['year']
        return redirect(url_for('leap_year', year=year))
    else:
        year = request.args.get('year')
        answer = None
        if year is not None:
            answer = check_if_leap_year(int(year))
        return render_template('leap_year.html', leap_years=leap_years, answer=answer, year=year)


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         return render_template('greetings.html', username=username)
#     else:
#         return render_template('login.html')


@app.route("/posts")
def posts():
    all_posts = Post.query.all()
    return render_template('posts.html', posts=all_posts)


@app.route('/posts/<string:post_id>')
def article(post_id):
    post = db.session.get(Post, post_id)
    return render_template('article.html', post=post)


@app.route('/posts/<string:post_id>/delete')
def delete_post(post_id):
    post_to_delete = db.session.get(Post, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    flash('Post has been deleted successfully!', 'success')
    return redirect(url_for('posts'))


@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    # form = PostForm()
    form = PostForm(formdata=MultiDict(request.form))
    # if form.validate_on_submit():
    if request.method == 'POST' and form.validate():
        post = Post(date=form.date.data,
                    title=form.title.data,
                    text=form.text.data,)
        # author_id=form.author_id.data)
        for author in form.authors.data:
            author = Author.query.get(author)
            post.authors.append(author)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts'))
    return render_template('create_post.html', title='New Post', form=form)
