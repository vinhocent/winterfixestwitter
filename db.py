import psycopg2
import os
import re
DATABASE_URL = os.environ['DATABASE_URL']

def db_create() -> None:

    
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS 
        globalData(
            currentconnection INT
        );
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS 
        msg(
            chat TEXT,
            sender TEXT,
            userName TEXT,
            puzzNum INT
        );
    """)
    
    cur.execute("""CREATE TABLE IF NOT EXISTS 
        userStats(
            userName TEXT,
            userMention TEXT,
            allClutches INT,
            allPerfect INT,
            allFails INT,
            allWins INT,
            UNIQUE(userMention)
        );
    """)
    conn.commit()
    cur.close()

    conn.close()

def dbinsertConnMsg(message,author) -> int:

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()
    
    pattern = r'\b\d+\b'

    match = re.search(pattern, message)
    puzzNum = 0
    if match : puzzNum = int(match.group(0))
    sql = "INSERT INTO msg (chat, sender, userName, puzzNum) VALUES (%s, %s, %s, %s)"
    val = (message, author.mention, author.name, puzzNum)
    cur.execute(sql,val)
    conn.commit()

    cur.close()
    conn.close()

    return puzzNum


def dbUpdateCurrent(puzzNum):

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()
    cur.execute("UPDATE globalData SET currentconnection = %s", (puzzNum,))
    conn.commit() 
    cur.close()
    conn.close()


def dbUpdateStats(author, isPerfect, isFail, isClutch, isWin):

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()
    cur.execute("""
        INSERT INTO userStats (username, userMention, allClutches, allPerfect, allFails, allWins)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (userMention) DO UPDATE
        SET allClutches = userStats.allClutches + EXCLUDED.allClutches, allPerfect= userStats.allPerfect + EXCLUDED.allPerfect, allFails = userStats.allFails + EXCLUDED.allFails , allWins = userStats.allWins + EXCLUDED.allWins   
        """, (author.name, author.mention, isClutch , isPerfect, isFail, isWin))

    conn.commit()
    cur.close()
    conn.close()

def viewStats(author):

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()
    cur.execute("SELECT * FROM userStats WHERE userMention = %s", (author.mention,))
    user_stats = cur.fetchone()
    print(user_stats)
    conn.commit()
    cur.close()
    conn.close()
    return user_stats[2] , user_stats[3], user_stats[4], user_stats[5]
    

