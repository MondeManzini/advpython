import sqlite3 as db
import traceback as tb
class UserDB(object):
    def __init__(self):
        self.conn = db.connect('userdb.sqlite')
        self.cur = self.conn.cursor()

    def query(self,sql,params=None):
        try:
            if params:
                self.cur.execute(sql,params)
            else:
                self.cur.execute(sql)
        except db.DatabaseError:
            print("Error in %s" % sql)
            print(tb.format_exc())
        else: print("query succeeded")

    def setup(self):
        sql = '''
           CREATE TABLE users(
           id INT PRIMARY KEY,
           username VARCHAR(64),
           password VARCHAR(64))
           '''
        self.query(sql)

    def add_user(self,id,username,password):
        sql = '''
            INSERT INTO users 
            VALUES(?, ?,?)'''
        self.cur.executemany(sql,[(id,username,password)])
        self.conn.commit()
    
    def showtable(self):
        sql = "SELECT * FROM users"
        self.query(sql)
        out = '\t'.join([x[0] for x in self.cur.description])
        for row in self.cur:
             out += '\n' + '\t'.join(map(str,row)) 
        return out     
        #for row in self.cur:
        #   print row

    def check_password(self, username, password):
        sql = "SELECT password FROM users WHERE username = '%s'" % username
        self.cur.execute(sql)
        return self.cur.fetchone()[0] == password


    def getcols(self):
        sql = "PRAGMA table_info('users')"
        self.query(sql)
        return self.cur.fetchall()

if __name__ == "__main__":
    userdb = UserDB()
    userdb.check_password('fred', 'qwerty')
    #userdb.addrow(4,'harry','qwerty')
    #print(userdb.showtable())

