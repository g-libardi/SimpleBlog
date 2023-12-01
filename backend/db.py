import sqlite3

conn = sqlite3.connect('database.sqlite', check_same_thread=False)
cur = conn.cursor()

class User:
    @staticmethod
    def _get_id(username):
        cur.execute('SELECT id FROM user WHERE username = ?', (username,))
        return cur.fetchone()[0]

    @staticmethod
    def create(name, username, password):
        if User.exists(username):
            return None
        cur.execute('INSERT INTO user (name, username, password) VALUES (?, ?, ?)', (name, username, password))
        conn.commit()
        return cur.lastrowid
    
    @staticmethod
    def get(username, *args):
        query = f'SELECT {", ".join(args)} FROM user WHERE username = ?'
        cur.execute(query, (username,))
        query = cur.fetchone()
        if query is None:
            return None
        data = {}
        for i, arg in enumerate(args):
            data[arg] = query[i]
        return data
            
    @staticmethod
    def get_username(user_id):
        cur.execute('SELECT username FROM user WHERE id = ?', (user_id,))
        return cur.fetchone()[0]
    
    @staticmethod
    def get_followers(username):
        user_id = User._get_id(username)
        cur.execute('SELECT username FROM user WHERE id IN (SELECT follower_id FROM follower WHERE user_id = ?)', (user_id,))
        return cur.fetchall()

    @staticmethod
    def get_following(username):
        user_id = User._get_id(username)
        cur.execute('SELECT username FROM user WHERE id IN (SELECT user_id FROM follower WHERE follower_id = ?)', (user_id,))
        return cur.fetchall()

    @staticmethod
    def follow(username, follower_username):
        user_id = User._get_id(username)
        follower_id = User._get_id(follower_username)
        cur.execute('INSERT INTO follower (user_id, follower_id) VALUES (?, ?)', (user_id, follower_id))
        conn.commit()
    
    @staticmethod
    def unfollow(username, follower_username):
        user_id = User._get_id(username)
        follower_id = User._get_id(follower_username)
        cur.execute('DELETE FROM follower WHERE user_id = ? AND follower_id = ?', (user_id, follower_id))
        conn.commit()
    
    @staticmethod
    def exists(username):
        return User.get(username, 'id') is not None
    

class Post:
    @staticmethod
    def create(content, username):
        user_id = User._get_id(username)
        cur.execute('INSERT INTO post (content, user_id) VALUES (?, ?)', (content, user_id))
        conn.commit()
        return cur.lastrowid
    
    @staticmethod
    def get(post_id):
        cur.execute('SELECT * FROM post WHERE id = ?', (post_id,))
        data = cur.fetchone()
        data = {
            'id': data[0],
            'content': data[1],
            'username': User.get_username(data[2]),
            'created_at': data[3]
        }
        return data
    
    @staticmethod
    def get_all():
        cur.execute('SELECT * FROM post ORDER BY created_at DESC')
        data = cur.fetchall()
        posts = []
        for post in data:
            posts.append({
                'id': post[0],
                'content': post[1],
                'username': User.get_username(post[2]),
                'created_at': post[3]
            })
        return posts
    
    @staticmethod
    def get_feed(username):
        user_id = User._get_id(username)
        cur.execute('SELECT * FROM post WHERE user_id IN (SELECT user_id FROM follower WHERE follower_id = ?)', (user_id,))
        return cur.fetchall()
    
    @staticmethod
    def delete(post_id):
        cur.execute('DELETE FROM post WHERE id = ?', (post_id,))
        conn.commit()

class Comment:
    @staticmethod
    def create(content, username, post_id):
        user_id = User._get_id(username)
        cur.execute('INSERT INTO comment (content, user_id, post_id) VALUES (?, ?, ?)', (content, user_id, post_id))
        conn.commit()
        return cur.lastrowid
    
    @staticmethod
    def from_post(post_id):
        cur.execute('SELECT * FROM comment WHERE post_id = ?', (post_id,))
        return cur.fetchall()
    
    @staticmethod
    def delete(comment_id):
        cur.execute('DELETE FROM comment WHERE id = ?', (comment_id,))
        conn.commit()
