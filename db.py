import mysql.connector
from login import *

db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cur = db.cursor()

def add_comment(id,uname,comments):
    query = "INSERT INTO bgxj2qxoat8r2vkjj0im.comments_table (content_id, uname, comments) VALUES (%s,%s,%s);"
    val = [id,uname,comments]
    cur.execute(query,val)
    db.commit()

def read_comments(content_id):
    query = "select * from bgxj2qxoat8r2vkjj0im.comments_table where content_id = %s;"
    cur.execute(query, [content_id])
    data = cur.fetchall()
    data = [list(i) for i in data]
    return data

