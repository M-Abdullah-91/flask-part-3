import pymysql

def mysqlconnect():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='google_keep_notes',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    print("db Connected")
    
    return conn


def disconnect(conn):
    conn.close()
    

if __name__ == "__main__":
    mysqlconnect()
    