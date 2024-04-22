import mysql.connector

class Db:
    def __init__(self):
        self.cnx = mysql.connector.connect(host="localhost",user="root",password="Pass@2023",database="fat_to_fit")
        self.cur = self.cnx.cursor(dictionary=True)

    def select(self, query, params=None):
        if params is not None:
            self.cur.execute(query, params)
        else:
            self.cur.execute(query)
        return self.cur.fetchall()

    # def select(self, q):
    #     self.cur.execute(q)
    #     return self.cur.fetchall()

    def selectOne(self, q):
        self.cur.execute(q)
        return self.cur.fetchone()

    def insert(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.lastrowid

    def update(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount

    def delete(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount
