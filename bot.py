import discord
from discord import app_commands
from discord.utils import get
import os
import responses
import asyncio
async def send_message(message,user_message,is_private):
    try:
        response,needDelete = responses.handle_response(user_message,message.author)

        if not needDelete and response != None: 
            await message.author.send(response) if is_private else await message.channel.send(response)
        if response != None and message.reference != None:
            repliedMessage = await message.channel.fetch_message(message.reference.message_id)
            await message.delete()
            await repliedMessage.reply(response, mention_author=True)
            
        elif response != None:
            await message.delete()
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
async def addRemoveSink(message, user : discord.Member):
    try:
        role = get(user.guild.roles, name="sink")
        if role.position >= user.top_role.position: #if the role is above users top role it sends error
            await message.channel.send('**:x: | That role is above your top role!**') 
        elif role in user.roles:
            await user.remove_roles(role) #removes the role if user already has
            await message.channel.send(f"Removed {role} from {user.mention}")
        else:
            await user.add_roles(role) #adds role if not already has it
            await message.channel.send(f"Added {role} to {user.mention}") 
    except Exception as e:
        print(e)
def run_discord_bot():

    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)
    @tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=745870568762638338)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
    async def first_command(interaction):
        await interaction.response.send_message("Hello!")
    # @tree.command(name = "connectstats", description = "Get your connections Stats!", guilds=[discord.Object(id=691001945447596114), discord.Object(id = 1050941726283534438)])   
    # async def getConnStats(interaction):
    #     response,needDelete = responses.handle_response("!connStats",interaction.user)
    #     await interaction.response.send_message(response)

    @tree.command(name='sync', description='Owner only')
    async def sync(interaction: discord.Interaction):
        if interaction.user.id == 96435974011105280:
            await tree.sync()
            print('Command tree synced.')
        else:
            await interaction.response.send_message('You must be the owner to use this command!')

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        
        await tree.sync(guild=discord.Object(id=691001945447596114))

        await tree.sync(guild=discord.Object(id=1050941726283534438))
        await client.change_presence(activity=discord.Streaming(name='Aespa - Drama', url='https://www.twitch.tv/tenz'))
        
        print("Ready!")



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
        elif user_message == "!sink":
            await addRemoveSink(message,message.author)
        elif user_message[0] == '?':
            user_message=user_message[1:]
            await send_message(message,user_message,is_private=True)
        else:
            await send_message(message,user_message,is_private=False)



    client.run(os.environ['TOKEN'])
