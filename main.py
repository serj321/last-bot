import discord
from dotenv import load_dotenv
import os
import random

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
        await message.channel.send("leave me the fuck alone")
    
    if message.content.startswith("$coin flip"):
        rand_num = random.randint(0, 1)
        if rand_num:
            await message.channel.send("heads")
        else:
            await message.channel.send("tails")
        


client.run(token)