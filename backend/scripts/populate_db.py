import sqlite3

conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()

cur.executescript('''
    INSERT INTO user (name, username, password) VALUES ('User 1', 'user1', 'password1');
    INSERT INTO user (name, username, password) VALUES ('User 2', 'user2', 'password2');
    INSERT INTO user (name, username, password) VALUES ('User 3', 'user3', 'password3');
    INSERT INTO user (name, username, password) VALUES ('User 4', 'user4', 'password4');
    INSERT INTO user (name, username, password) VALUES ('User 5', 'user5', 'password5');
    INSERT INTO user (name, username, password) VALUES ('TestUser', 'TestUser', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');

    INSERT INTO follower (user_id, follower_id) VALUES (1, 2);
    INSERT INTO follower (user_id, follower_id) VALUES (1, 3);
    INSERT INTO follower (user_id, follower_id) VALUES (1, 4);
    INSERT INTO follower (user_id, follower_id) VALUES (1, 5);
    INSERT INTO follower (user_id, follower_id) VALUES (2, 1);
    INSERT INTO follower (user_id, follower_id) VALUES (2, 3);
    INSERT INTO follower (user_id, follower_id) VALUES (2, 4);
    INSERT INTO follower (user_id, follower_id) VALUES (2, 5);
    INSERT INTO follower (user_id, follower_id) VALUES (3, 1);
    INSERT INTO follower (user_id, follower_id) VALUES (3, 2);
    INSERT INTO follower (user_id, follower_id) VALUES (3, 4);
    INSERT INTO follower (user_id, follower_id) VALUES (3, 5);
    INSERT INTO follower (user_id, follower_id) VALUES (4, 1);
    INSERT INTO follower (user_id, follower_id) VALUES (4, 2);
    INSERT INTO follower (user_id, follower_id) VALUES (4, 3);
    INSERT INTO follower (user_id, follower_id) VALUES (4, 5);
    INSERT INTO follower (user_id, follower_id) VALUES (5, 1);
    INSERT INTO follower (user_id, follower_id) VALUES (5, 2);
    INSERT INTO follower (user_id, follower_id) VALUES (5, 3);
    INSERT INTO follower (user_id, follower_id) VALUES (5, 4);

    INSERT INTO post (content, user_id) VALUES ('Hello world!', 1);
    INSERT INTO post (content, user_id) VALUES ('Another post', 1);
    INSERT INTO post (content, user_id) VALUES ('Hello world!', 2);
    INSERT INTO post (content, user_id) VALUES ('Another post', 2);
    INSERT INTO post (content, user_id) VALUES ('Hello world!', 3);
    INSERT INTO post (content, user_id) VALUES ('Another post', 3);
    INSERT INTO post (content, user_id) VALUES ('Hello world!', 4);
    INSERT INTO post (content, user_id) VALUES ('Another post', 4);
    INSERT INTO post (content, user_id) VALUES ('Hello world!', 5);
    INSERT INTO post (content, user_id) VALUES ('Another post', 5);

    INSERT INTO comment (content, user_id, post_id) VALUES ('Nice post!', 2, 1);
    INSERT INTO comment (content, user_id, post_id) VALUES ('I agree!', 3, 1);
    INSERT INTO comment (content, user_id, post_id) VALUES ('Nice post!', 1, 3);
    INSERT INTO comment (content, user_id, post_id) VALUES ('I agree!', 4, 3);
    INSERT INTO comment (content, user_id, post_id) VALUES ('Nice post!', 1, 5);
    INSERT INTO comment (content, user_id, post_id) VALUES ('I agree!', 2, 5);
    INSERT INTO comment (content, user_id, post_id) VALUES ('Nice post!', 3, 7);
    INSERT INTO comment (content, user_id, post_id) VALUES ('I agree!', 1, 7);
    INSERT INTO comment (content, user_id, post_id) VALUES ('Nice post!', 4, 9);
    INSERT INTO comment (content, user_id, post_id) VALUES ('I agree!', 1, 9);
''')

conn.commit()
conn.close()
