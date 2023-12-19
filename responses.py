import os
import psycopg2
import db
from typing import Optional

urlReplaceDict = {
    "https://x.com/": "https://fxtwitter.com/",
    "https://twitter.com/": "https://fxtwitter.com/",
    "https://instagram.com/": "https://ddinstagram.com/",
    "https://tiktok.com/": "https://vxtiktok.com/",
    "https://pixiv.net/": "https://phixiv.net/"
}

def handle_response(message, author) -> Optional[str]:
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
        
        db.db_create()
        puzzNum = db.dbinsertConnMsg(message,author)
        

        return
