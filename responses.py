import re
def handle_response(message) -> str:
    p_message = message.lower()
    if 'https://x.com/' in p_message:
        tweet = re.search("(?P<url>https?://[^\s]+)", p_message).group("url")
        reply = tweet.replace('https://x.com', 'https://fxtwitter.com')
        print(reply)
        return reply
    
    if 'https://twitter.com/' in p_message:
        tweet = re.search("(?P<url>https?://[^\s]+)", p_message).group("url")
        reply = tweet.replace('https://twitter.com', 'https://fxtwitter.com')
        return reply
    
    if p_message == "!winter":
        return "I'm Winter byum blum buh"