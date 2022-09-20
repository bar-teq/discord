import discord
from discord.ext import tasks, commands


class Cogcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("cog commands loaded")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "lol":
            await message.delete()
            await message.channel.send("smieszne w chuj")


async def setup(bot: commands.Bot):
    await bot.add_cog(Cogcommands(bot))
