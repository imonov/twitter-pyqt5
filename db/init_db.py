import pymysql


class MySQL:
    def __init__(self):
        self.connect()
        self.createDatabase()
        self.createUsersTable()
        # self.createPostsTable()
        self.insertTestUser()

    def connect(self):
        try:
            self.db = pymysql.connect(
                host="localhost",
                user="root",
                password="1234"
            )
            self.cur = self.db.cursor()
        except:
            print("DB'ga ulanmadi")
            return

    def createDatabase(self):
        self.cur.execute("CREATE DATABASE IF NOT EXISTS twitgram;")
        self.cur.execute("USE twitgram")

    def createUsersTable(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(30) NOT NULL UNIQUE,
                fullname VARCHAR(50) NOT NULL,
                password VARCHAR(32) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );     
        ''')

    # def createPostsTable(self):
    #     self.cur.execute('''
    #         CREATE TABLE IF NOT EXISTS posts(
    #             id INT AUTO_INCREMENT PRIMARY KEY,
    #             title VARCHAR(100) NOT NULL,
    #             post_text TEXT NOT NULL,
    #             author_id INT,
    #             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP),
    #             FOREIGN KEY (author_id) REFERENCES users(id)
    #         );
    # ''')

    def insertTestUser(self):
        self.cur.execute('''
            INSERT INTO users(username, password, fullname) 
            VALUES("test", "test123", "Test User");              
        ''')
        self.db.commit()


if __name__ == "__main__":
    my = MySQL()
