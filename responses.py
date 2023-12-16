import re
import os
import psycopg2


urlReplaceDict = {
    "https://x.com/": "https://fxtwitter.com/",
    "https://twitter.com/": "https://fxtwitter.com/",
    "https://instagram.com/": "https://ddinstagram.com/",
    "https://tiktok.com/": "https://vxtiktok.com/",
    "https://pixiv.net/": "https://phixiv.net/"
}

def handle_response(message, author) -> str:
    for originalUrl in urlReplaceDict:
        if originalUrl in message:
            reply = message.replace(originalUrl, urlReplaceDict[originalUrl])  
            return author.mention+ ": " + reply

    if message == "!winter":
        return "I'm Winter byum blum buh"
    if message == "!saranghae":
        return "Saranghae!"
    if "huzaifa" in message.lower() or "huz" in message.lower():
        return "rest in peace"

    if "Connections \nPuzzle #" in message:
        DATABASE_URL = os.environ['DATABASE_URL']

        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS 
            msg(
                chat TEXT,
                sender TEXT,
                userName TEXT
            );
        """)

        sql = "INSERT INTO msg (chat, sender) VALUES (%s, %s)"
        val = (message, author.mention, author.name)
        cur.execute(sql,val)
        conn.commit()

        cur.close()
        conn.close()

