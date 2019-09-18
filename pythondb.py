import sqlite3


class Sqlite3_db:
    def __init__(self,database1='Publisher.db',database2='Book.db',database3='Author.db'):
        self.database1=database1
        self.conn1=sqlite3.connect(self.database1)
        self.publisher=self.conn1.cursor()

        self.database2=database2
        self.conn2=sqlite3.connect(self.database2)
        self.book=self.conn2.cursor()

        self.database3=database3
        self.conn3=sqlite3.connect(self.database3)
        self.author=self.conn3.cursor()

    def create_table(self):
        self.publisher.execute('CREATE TABLE IF NOT EXISTS Publisher(Name TEXT(50),Address TEXT(200),Phone INTEGER,URL TEXT(50))')
        self.conn1.commit()

        self.book.execute('CREATE TABLE IF NOT EXISTS book(ISBN VARCHAR(255),Publisher_Name TEXT(50),Author_Name TEXT(200),Author_Address TEXT(100),year INTEGER,Title TEXT(50),Price INTEGER)')
        self.conn2.commit()

        self.author.execute('CREATE TABLE IF NOT EXISTS author(Name TEXT(40),Address TEXT(100),URL TEXT(30))')
        self.conn3.commit()

    def insert(self):
        self.publisher.execute('INSERT INTO Publisher VALUES("Ali Shakoori","Meydan gorgan",09127171637,"Alishakoori89@gmail.com")')  
        self.conn1.commit()
        self.conn1.close()

obj=Sqlite3_db()
obj.create_table()
obj.insert()