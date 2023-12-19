import psycopg2
import os
import re
DATABASE_URL = os.environ['DATABASE_URL']
def db_create() -> None:

    
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS 
        msg(
            chat TEXT,
            sender TEXT,
            userName TEXT
        );
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS 
        metadata(
            currentConnections INT(255),
        );
    """)
    

    conn.close()

    conn.close()

def dbinsertConnMsg(message,author) -> int:

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()
    
    pattern = r'\b\d+\b'

    match = re.search(pattern, message)
    puzzNum = 0
    if match : puzzNum = int(match.group(0))
    sql = "INSERT INTO msg (chat, sender, userName, puzzNum) VALUES (%s, %s, %s, %i)"
    val = (message, author.mention, author.name, puzzNum)
    cur.execute(sql,val)
    conn.commit()

    cur.close()
    conn.close()

    return puzzNum
