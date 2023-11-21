import pymysql

def mysqlconnect():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='googlenotes',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    
    return conn


def disconnect(conn):
    conn.close()
    

if __name__ == "__main__":
    mysqlconnect()
    