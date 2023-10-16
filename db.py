import mysql.connector

class Database:

    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='nlp_web_app')
        self.cursor = self.conn.cursor()

    def select(self, email, password):
        self.cursor.execute('''
        SELECT * FROM `users`
        WHERE `email` LIKE '{}' AND `password` LIKE '{}'
        '''.format(email, password))

        users = self.cursor.fetchall()

        return users

    def insert(self, name, email, password):
        self.cursor.execute('''
        SELECT * FROM `users`
        WHERE `email` LIKE '{}'
        '''.format(email))

        users = self.cursor.fetchall()

        if len(users) > 0:
            return 0

        else:
            self.cursor.execute('''
            INSERT INTO `users` (`user_id`, `name`, `email`, `password`)
            VALUES (NULL, '{}', '{}', '{}')
            '''.format(name, email, password))

            self.conn.commit()

            return 1