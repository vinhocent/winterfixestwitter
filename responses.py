import os
import psycopg2
import db
from typing import Optional
import connHelpers
import random

urlReplaceDict = {
    "https://x.com/": "https://fixupx.com/",
    "https://twitter.com/": "https://fixup.com/",
    "instagram.com/": "https://ddinstagram.com/",
    "https://tiktok.com/": "https://vxtiktok.com/",
    "https://pixiv.net/": "https://phixiv.net/"
}

kaomojiDict = {
    1: "(◕‿◕✿)", 
    2: "(✿╹◡╹)",
    3: "(◕ᴥ◕)",
    4: "(´｡• ᵕ •｡`) ♡",
    5: "♡＼(￣▽￣)／♡",
    6: "(o^▽^o)",
    7: "٩(◕‿◕｡)۶",
    8: "o(>ω<)o",
    9: "\(★ω★)/",
    10: "(☆ω☆)"

}

def handle_response(message, author):
    for originalUrl in urlReplaceDict:
        if originalUrl in message:
            reply = message.replace(originalUrl, urlReplaceDict[originalUrl])  
            return author.mention+ ": " + reply , True

    if message == "!winter":
        return "I'm Winter byum blum buh" , True
    if message == "!saranghae":
        return "Saranghae!", True
    if "huzaifa" in message.lower() or "huz" in message.lower():
        return "rest in peace" , False
    if "!connStats" == message:
        allClutch, allPerfect, allFail , allWin = db.viewStats(author)
        return connHelpers.printStats(author.mention, allPerfect, allFail, allClutch, allWin), True
    if "Connections \nPuzzle #" in message:
        
        # db.db_create()
        # puzzNum = db.dbinsertConnMsg(message,author)
        # db.dbUpdateCurrent(puzzNum)
        isPerfect, isFail, isClutch, isWin = connHelpers.getStats(message)
        # db.dbUpdateStats(author, isPerfect,isFail, isClutch, isWin)


        if (isFail):
            return "NT doglet " + author.mention, False

        if (isPerfect):
            randomEmoji = random.randint(1,len(kaomojiDict))
            return f"WOW PERFECT! {kaomojiDict[randomEmoji]} GOOD JOB " + author.mention, False

        if (isClutch):
            return ("Whew, you clutched up! " + author.mention ) , False

    return None, False
