import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import Select, View


# load env variable to get the bot token
load_dotenv()
token = os.environ.get("TOKEN")

# Define intents
intents = discord.Intents.default()  # This enables the default intents, including guilds and messages
intents.messages = True  # Enable the bot to receive messages
# If your bot needs to track presence or member events, you might also need intents.presences = True or intents.members = True

# Create a bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is online")

class MySelect(View):

    @discord.ui.select(
        placeholder="Choose an option",
        options=[
            discord.SelectOption(label="Red", value="1", description="Select this for red"),
            discord.SelectOption(label="Blue", value="2", description="Select this for blue"),
            discord.SelectOption(label="Green", value="3", description="Select this for green")
        ]
    )

    async def select_callback(self, select, interaction):
        select.disabled=True
        if select.values[0] == "1":
            em = discord.Embed()
            em.set_author(name="this a edited embed")
            em.add_field(name="Civo", value="test sub", inline=False)
            await interaction.response.edit_message(embed=em)
        if select.values[0] == "2":
            await interaction.response.edit_message(content="edited text")
        if select.values[0] == "3":
            await interaction.response.edit_message(content="we edit")
        
@bot.command()
async def menu(ctx):
    view = MySelect()
    await ctx.send("Hello", view=view)


# Run the bot with your token
bot.run(token)
