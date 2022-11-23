import discord
from discord.ext import tasks, commands
import random


class Cogcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("COMMANDS loaded")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, no_of_lines=5):
        await ctx.channel.purge(limit=no_of_lines)

    # @commands.command()
    # async def papiez(self, ctx):
    #     await ctx.message.delete()
    #     await ctx.channel.send('https://tenor.com/view/jp2gmd-pope-dance-gif-8448985')

    @commands.command()
    async def add_cytat(self, ctx, cytat):
        with open('/home/carmel/discobot/links/cytat.txt', 'a') as f:
            f.write(f"{cytat} \n")
        await ctx.channel.send('cytat dodany')

    @commands.command()
    async def cytat(self, ctx):
        with open("/home/carmel/discobot/links/cytat.txt", "r") as f:
            urls = f.readlines()
            await ctx.channel.send(random.choice(urls))


async def setup(bot: commands.Bot):
    await bot.add_cog(Cogcommands(bot))
