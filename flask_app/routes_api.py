from flask import request, jsonify
from flask_app import app, db
from .models import Post, Author
from datetime import datetime


# authors API
@app.route('/api/authors/new', methods=['POST'])
def add_author():
    data = request.get_json()
    author = Author(name=data['name'],
                    nationality=data['nationality'],
                    phone=data['phone'],
                    email=data['email'])
    db.session.add(author)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Author added successfully'})


@app.route('/api/authors', methods=['GET'])
def get_all_authors():
    all_authors = Author.query.all()
    result = [author.to_dict() for author in all_authors]
    return jsonify(result)


@app.route('/api/author/<author_id>', methods=['GET'])
def get_author(author_id):
    author = Author.query.get(author_id)
    result = author.to_dict()
    return jsonify(result)


@app.route('/api/authors/<author_id>', methods=['PUT'])
def edit_author(author_id):
    author = Author.query.get(author_id)
    # author.name = request.json.get('name', author.name)
    # author.nationality = request.json.get('nationality', author.nationality)
    # author.phone = request.json.get('phone', author.phone)
    # author.email = request.json.get('email', author.email)
    update_dict = request.json
    for key, value in update_dict.items():
        setattr(author, key, value)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Author was updated successfully'})


@app.route('/api/authors/<author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = Author.query.get(author_id)
    db.session.delete(author)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Author deleted successfully'})


# posts API
@app.route('/api/posts/new', methods=['POST'])
def add_post():
    data = request.get_json()
    date = datetime.strptime(data['date'], '%Y-%m-%d').date()
    post = Post(date=date,
                title=data['title'],
                text=data['text'])
    if data.get('authors'):
        author_ids = [int(x.strip()) for x in data['authors'].split(',')]
        for author_id in author_ids:
            author = Author.query.get(author_id)
            post.authors.append(author)
    db.session.add(post)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Post added successfully'})
