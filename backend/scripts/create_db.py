import sqlite3 

conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
for table in tables:
    if table[0] == 'sqlite_sequence':
        continue
    cur.execute('DROP TABLE IF EXISTS ' + table[0])

cur.executescript('''
    CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE follower (
        user_id INTEGER NOT NULL,
        follower_id INTEGER NOT NULL,
        PRIMARY KEY (user_id, follower_id),
        FOREIGN KEY (user_id) REFERENCES user (id),
        FOREIGN KEY (follower_id) REFERENCES user (id)
    );

    CREATE TABLE post (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user (id)
    );

    CREATE TABLE comment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        user_id INTEGER NOT NULL,
        post_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user (id),
        FOREIGN KEY (post_id) REFERENCES post (id)
    );
''')

conn.commit()
conn.close()