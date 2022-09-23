import discord
from discord.ext import tasks, commands


class Cogcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("COMMANDS loaded")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx):
        await ctx.channel.purge(limit=5)

    @commands.command()
    async def papiez(self, ctx):
        await ctx.message.delete()
        await ctx.channel.send('https://tenor.com/view/jp2gmd-pope-dance-gif-8448985')


async def setup(bot: commands.Bot):
    await bot.add_cog(Cogcommands(bot))
