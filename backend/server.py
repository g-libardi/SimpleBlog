from flask import Flask, request, jsonify
from flask_cors import CORS
import user_manager as auth
import db

app = Flask(__name__)
CORS(app)

def auth(username, token):
    if auth.auth(username, token):
        user_info = db.User.get(username, 'username', 'name')
        return jsonify(user_info), 200

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
    if content is None or content == '':
        return jsonify({'error': 'Post cannot be empty'}), 400
    
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

@app.route('/u/<username>', methods=['GET'])
def user(username):
    user = db.User.get(username, 'username', 'name')
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200

@app.route('/u/<username>/followers', methods=['GET'])
def followers(username):
    followers = db.User.get_followers(username)
    if followers is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(followers), 200

@app.route('/u/<username>/following', methods=['GET'])
def following(username):
    following = db.User.get_following(username)
    if following is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(following), 200

@app.route('/u/<username>/follow', methods=['POST'])
def follow(username):
    data = request.get_json()
    follower_username = data['follower_username']
    token = data['token']
    if auth.auth(username, token):
        db.User.follow(username, follower_username)
        return jsonify({'message': 'User followed successfully'}), 200
    return jsonify({'error': 'Invalid token'}), 401

@app.route('/u/<username>/unfollow', methods=['POST'])
def unfollow(username):
    data = request.get_json()
    current_user = data['auth']['username']
    token = data['token']
    if auth.auth(username, token):
        db.User.unfollow(username, current_user)
        return jsonify({'message': 'User unfollowed successfully'}), 200
    return jsonify({'error': 'Invalid token'}), 401

@app.route('/u/<username>/posts', methods=['GET'])
def user_posts(username):
    posts = db.Post.get_user_posts(username)
    if posts is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'posts': posts}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
