import re

urlReplaceDict = {
    "https://x.com/": "https://fxtwitter.com/",
    "https://xwitter.com/": "https://fxtwitter.com/",
    "https://xnstagram.com/": "https://ddinstagram.com/"
    "https://xiktok.com/": "https://vxtiktok.com/"
    "https://xpixiv.net/": "https://phixiv.net/"
}

def handle_response(message, author) -> str:
    # if 'https://x.com/' in message:
    #     reply = message.replace('https://x.com', 'https://fxtwitter.com')
    #     return author.mention+ ": " + reply
    #
    # if 'https://twitter.com/' in message:
    #     reply = message.replace('https://twitter.com', 'https://fxtwitter.com')
    #     return author.mention+ ": " + reply
    #
    # if 'instagram.com/' in message:
    #     # tweet = re.search("(?P<url>https?://[^\s]+)", p_message).group("url")
    #     reply = message.replace('instagram.com', 'ddinstagram.com')
    #     return author.mention+ ": " + reply
    #
    #
    # if 'tiktok.com/' in message:
    #     reply = message.replace('tiktok.com', 'vxtiktok.com')
    #     return author.mention+ ": " + reply
    #
    #
    #
    # if 'pixiv.net/' in message:
    #     reply = message.replace('pixiv.net', 'phixiv.net')
    #     return author.mention+ ": " + reply
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
