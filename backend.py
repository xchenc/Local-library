import sqlite3
class library:
    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, title text, author text, year integer,isbn integer )")
        self.conn.commit()
        self.conn.close()

    def insert(self,title, author, year, isbn):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO library VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
        self.conn.commit()
        self.conn.close()

    def view(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("Select * from library")
        res = self.cur.fetchall()
        self.conn.close()
        return res

    def search(self,title="",author="",year="",isbn=""):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("Select * from library where title = ? or author = ? or year = ? or isbn = ?", (title,author,year,isbn))
        res = self.cur.fetchall()
        self.conn.close()
        return res


    def delete(self,id):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("Delete from library where id=?", (id,))
        self.conn.commit()
        self.conn.close()

    def update(self,d,title,author,year,isbn):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE library set title =?, author = ?, year = ?, isbn = ? where id=?", (title,author,year,isbn,id))
        self.conn.commit()
        self.conn.close()




# connect()
# insert("book1","aav","1997","0010001")
# delete(3)
# update(2,'updatebookname','xian', 1997, 2222)
# print(view())
# print(search(author='xian'))
