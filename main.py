import discord
from dotenv import load_dotenv
import os
import random
import steam_requests

print("starting bot...")

# load env variable to get the bot token
load_dotenv()
token = os.environ.get("TOKEN")

# setting up discord bot with intents
set_intents = discord.Intents.default()
set_intents.message_content = True
client = discord.Client(intents=set_intents)

@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("hi there")
    
    if message.content.startswith("$coin flip"):
        rand_num = random.randint(0, 1)
        if rand_num:
            await message.channel.send("heads")
        else:
            await message.channel.send("tails")

    if message.content.startswith("$steam players"):
        app_name = message.content[15:]
        player_count = steam_requests.get_current_steam_players(app_name)
        await message.channel.send(f"there are {player_count} playing {app_name} at this moment.")
    elif message.content.startswith("$steam"):
        app_name = message.content[7:]
        app_id = steam_requests.get_steam_app_id(app_name)
        await message.channel.send(f"The app ID for {app_name} is: {app_id}")
        



client.run(token)