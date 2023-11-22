import db
from datetime import date
from flask import request
import jwt

def register(data):
    username = data['user_name']
    email = data['email']
    password = data['password']
    
    db_conn = db.mysqlconnect()
    cursor = db_conn.cursor()
    
    query = "INSERT INTO users(user_name,email,password,created_at) VALUES (%s, %s, %s,%s)"
    values = (username, email, password,date.today())
    
    cursor.execute(query, values)
    db_conn.commit()

    return "Added"

def login(data):
    email = data['email']
    password = data['password']

    db_conn = db.mysqlconnect()
    cursor = db_conn.cursor()

    query = "SELECT * FROM users WHERE email=%s AND password=%s "
    values = (email,password)

    cursor.execute(query,values)
    db_conn.commit()

    response = cursor.fetchone()
    return response



def add_notes(data):
        title = data['title']
        desc = data['description']

        token=request.headers.get('Authorization')
        decoded_token=jwt.decode(token,'THISISSECRETKEY',algorithms=['HS256'])


        db_conn = db.mysqlconnect()
        cursor = db_conn.cursor()

        query = "INSERT INTO notes(title,description,user_id,created_at) VALUES (%s,%s,%s,%s)"
        created_at = date.today()
        values = title,desc,decoded_token['id'],created_at

        cursor.execute(query,values)
        db_conn.commit()

        response = cursor.fetchone()
        return response

def assign_note_category(data):
     
    categoryid = data['category_id']
    notes_id = data['notes_id']

    token=request.headers.get('Authorization')
    decoded_token=jwt.decode(token,'THISISSECRETKEY',algorithms=['HS256'])

    db_conn = db.mysqlconnect()
    cursor = db_conn.cursor()

    query = "INSERT INTO notes_category(notes_id,category_id,created_at) VALUES (%s,%s,%s)"
    created_at = date.today()
    values = notes_id,categoryid,created_at

    cursor.execute(query,values)
    db_conn.commit()

    response = cursor.fetchone()
    return response


def view_notes():
    
    token=request.headers.get('Authorization')
    decoded_token=jwt.decode(token,'THISISSECRETKEY',algorithms=['HS256'])

    db_conn = db.mysqlconnect()
    cursor = db_conn.cursor()

    query = "SELECT * FROM notes WHERE user_id=%s"
    values = decoded_token['id']

    cursor.execute(query,values)
    db_conn.commit()

    response = cursor.fetchall()
    return response 
     
def get_notes_by_category(data):
    category_name= data['category_name']

    db_conn = db.mysqlconnect()
    cursor = db_conn.cursor()

    query = """select n.title,n.description,c.name as category_name from notes as n 
                inner join notes_category as nc
                on n.id = nc.notes_id
                inner join category as c
                on c.id = nc.category_id where c.name=%s"""
    
    values = category_name

    cursor.execute(query,values)
    db_conn.commit()

    response = cursor.fetchall()
    return response 

def add_category(data):
        name = data['name']
        created_at = date.today()

        db_conn = db.mysqlconnect()
        cursor = db_conn.cursor()

        query = "INSERT INTO category(name,created_at) VALUES (%s,%s)"
        values = name,created_at

        cursor.execute(query,values)
        db_conn.commit()

        response = cursor.fetchone()
        return response
