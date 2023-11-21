import db
from datetime import date


def register(data):
    username = data['user_name']
    email = data['email']
    password = data['password']
    
    db_conn = db.mysqlconnect()
    cursor = db_conn.cursor()
    
    query = "INSERT INTO users(user_name,email,password) VALUES (%s, %s, %s,%s)"
    values = (username, email, password,date.today())
    
    cursor.execute(query, values)
    
    db_conn.commit()
    db_conn.close()

    return cursor.lastrowid