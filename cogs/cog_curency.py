import discord
from discord.ext import tasks, commands


class Currencies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Curencies loaded")


async def setup(bot: commands.Bot):
    await bot.add_cog(Currencies(bot))
