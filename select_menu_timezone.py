from discord.ui import Select, View
from discord.ext import commands
import discord

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
        
@client.command()
async def menu(ctx):
    view = MySelect()
    await ctx.send("Hello", view=view)

