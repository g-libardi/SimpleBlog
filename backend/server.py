from flask import Flask, request, jsonify
from flask_cors import CORS
import user_manager as auth
import db

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print(username, password)
    token = auth.sign_in(username, password)
    if token is None:
        return jsonify({'error': 'Invalid username or password'}), 401
    return jsonify({'token': token}), 200

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data['name']
    username = data['username']
    password = data['password']
    if auth.sign_up(name, username, password):
        return jsonify({'message': 'User created successfully'}), 201
    return jsonify({'error': 'Username already exists'}), 409

@app.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    username = data['username']
    token = data['token']
    if auth.sign_out(token, username):
        return jsonify({'message': 'User logged out successfully'}), 200
    return jsonify({'error': 'Invalid token'}), 401

@app.route('/new_post', methods=['POST'])
def new_post():
    data = request.get_json()
    username = data['username']
    token = data['token']
    content = data['content']
    
    if auth.auth(username, token):
        post_id = db.Post.create(content, username)
        post = db.Post.get(post_id)
        return jsonify(post), 201
    return jsonify({'error': 'Invalid token'}), 401

@app.route('/posts', methods=['GET'])
def posts():
    posts = db.Post.get_all()
    if posts is None:
        return jsonify({'error': 'No posts found'}), 404
    return jsonify(posts), 200


if __name__ == '__main__':
    # check if windows system
    import os
    if os.name == 'nt':
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        from gunicorn.app.wsgiapp import WSGIApplication
        WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()
