import re
def handle_response(message, author) -> str:
    if 'https://x.com/' in message:
        # tweet = re.search("(?P<url>https?://[^\s]+)", p_message).group("url")
        reply = message.replace('https://x.com', 'https://fxtwitter.com')
        return author.mention+ ": " + reply
    
    if 'https://twitter.com/' in message:
        # tweet = re.search("(?P<url>https?://[^\s]+)", p_message).group("url")
        reply = message.replace('https://twitter.com', 'https://fxtwitter.com')
        return author.mention+ ": " + reply
    
    if 'instagram.com/' in message:
        # tweet = re.search("(?P<url>https?://[^\s]+)", p_message).group("url")
        reply = message.replace('instagram.com', 'ddinstagram.com')
        return author.mention+ ": " + reply

    if message == "!winter":
        return "I'm Winter byum blum buh"

    if message == "!saranghae":
        return "Saranghae!"
    if "huzaifa" in message.lower() or "huz" in message.lower():
        return "rest in peace"
