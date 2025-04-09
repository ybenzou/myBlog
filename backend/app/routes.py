from flask import Blueprint, jsonify, request
from .models import db, Post

main = Blueprint('main', __name__)

@main.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': p.id, 'title': p.title, 'body': p.body} for p in posts])

@main.route('/api/post/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({'id': post.id, 'title': post.title, 'body': post.body})

@main.route('/api/post', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'], body=data['body'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post created', 'id': new_post.id}), 201

@main.route('/api/post/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted'}), 200
