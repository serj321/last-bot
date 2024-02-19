import discord
from dotenv import load_dotenv
import os

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

client.run(token)