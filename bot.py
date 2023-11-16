import discord
import os
import responses

async def send_message(message,user_message,is_private):
    try:
        response = responses.handle_response(user_message,message.author)
        if (response != None):
            await message.delete()
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)



    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Aespa - Drama", url = "https://open.spotify.com/track/5XWlyfo0kZ8LF7VSyfS4Ew?si=b686e4664c5c432a"))


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if len(message.attachments) > 0 and user_message == "":
            
            return
        # print(f"{username} said: '{user_message}' ({channel})")
        elif user_message[0] == '?':
            user_message=user_message[1:]
            await send_message(message,user_message,is_private=True)
        else:
            await send_message(message,user_message,is_private=False)


    client.run(os.environ['TOKEN'])
