import pymysql


class MySQL:
    def __init__(self):
        self.connectDb()

    def connectDb(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="twitgram"
        )

        self.cur = self.db.cursor()

    def createUser(self, username, password, fullname):
        self.cur.execute(
            f'''INSERT INTO users(username, password, fullname)  VALUES ("{username}", "{password}", "{fullname}");''')
        self.db.commit()

    def loginUser(self, username):
        self.cur.execute(
            f'''SELECT id, username, password FROM users WHERE username = "{username}";''')
        return self.cur.fetchone()

    def deleteUser(self, id, username):
        self.cur.execute(
            f'''DELETE FROM users WHERE id = {id} AND username = "{username}";''')
        self.db.commit()

    def createPost(self, id, title, post_text):
        self.cur.execute(
            f'''INSERT INTO posts(title, post_text, author_id) VALUES ("{title}", "{post_text}", {id});''')
        self.db.commit()

    def getPosts(self):
        self.cur.execute(f'''
            SELECT title, post_text, p.created_at, u.fullname FROM posts as p JOIN users AS u ON p.author_id = u.id                  
        ''')

        return self.cur.fetchall()
