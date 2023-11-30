import hashlib
import secrets
from db import User

sessions = {}

def _hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def _generate_session_token():
    return secrets.token_hex(16)

def sign_up(name, username, password):
    if User.exists(username):
        return False
    User.create(name, username, _hash_password(password))
    return True

def sign_in(username, password):
    if not User.exists(username):
        return None
    user = User.get(username, 'id', 'password')
    if user['password'] == _hash_password(password):
        session_token = _generate_session_token()
        add_session(session_token, user['id'])
        return session_token
    return None

def add_session(session_token, user_id):
    token_list = sessions.get(user_id, [])
    token_list.append(session_token)
    sessions[user_id] = token_list

def sign_out(session_token, username):
    user_id = User.get(username, 'id')['id']
    token_list = sessions.get(user_id, [])
    if session_token in token_list:
        token_list.remove(session_token)
        sessions[user_id] = token_list
        return True
    return False

def auth(username, session_id):
    if not User.exists(username):
        return False
    user_id = User.get(username, 'id')['id']
    return session_id in sessions.get(user_id, [])
                                      

if __name__ == '__main__':
    print(sign_up('John Doe', 'johndoe', 'password'))
    token = sign_in('johndoe', 'password')
    print(token)
    print(auth('johndoe', token))
    print(sign_out(token, 'johndoe'))
    print(auth('johndoe', token))