import sqlite3


class Sqlite3_db:
    def __init__(self,database='BookSQL.db'):
        self.database=database
        self.conn=sqlite3.connect(self.database)
        self.cur=self.conn.cursor()

    def create_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS Publisher(pID INTEGER PRIMARY KEY AUTOINCREMENT,PName TEXT(50),Address TEXT(200),Phone INTEGER,URL TEXT(50))')
        self.conn.commit()

        self.cur.execute('CREATE TABLE IF NOT EXISTS book(bID INTEGER PRIMARY KEY AUTOINCREMENT,pID INTEGER,aID INTEGER,ISBN INTEGER,Publisher_Name TEXT(50),Author_Name TEXT(200),Author_Address TEXT(100),year INTEGER,Title TEXT(50),Price INTEGER,FOREIGN KEY (pID) REFERENCES Publisher (pID),FOREIGN KEY (aID) REFERENCES author (aID))')
        self.conn.commit()

        self.cur.execute('CREATE TABLE IF NOT EXISTS author(aID INTEGER PRIMARY KEY AUTOINCREMENT,AName TEXT(40),Address TEXT(100),URL TEXT(80))')
        self.conn.commit()

    def insert(self):
        self.cur.execute('INSERT INTO Publisher VALUES(1,"Ali Shakoori","Meydan gorgan",09127171637,"Alishakoori89@gmail.com")')  
        self.cur.execute('INSERT INTO book VALUES(1,1,1,123,"َAmir Lesani","Surush Mehmandoost","tehran dabestan",1370/05/07,"kosesherhaye sooroosh",200000)') 
        self.cur.execute('INSERT INTO author VALUES(1,"Surush Mehmandoos","tehran dabestan","surushmehmandoos_Author@gmail.com")')
        self.conn.commit()

    def select(self):
        print('kosesherhaye sooroosh book title Author URL link :')
        self.x=self.cur.execute('SELECT URL FROM author WHERE aID IN (SELECT aID FROM book WHERE Title="kosesherhaye sooroosh")')

        self.x=self.cur.fetchall()
        print(self.x)
obj=Sqlite3_db()
obj.create_table()
obj.insert()
obj.select()