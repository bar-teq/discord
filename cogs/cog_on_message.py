import asyncio
import discord
from discord.ext import tasks, commands


class Onmsg_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("cog onmsgs loaded")

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        if str(after.status) == 'online':
            print("cos sie dzieje")
            await self.bot.get_channel(993905352498221066).send("test")

    @commands.command()
    async def papiez(self, ctx):
        await ctx.message.delete()
        await ctx.channel.send('https://tenor.com/view/jp2gmd-pope-dance-gif-8448985')


async def setup(bot: commands.Bot):
    await bot.add_cog(Onmsg_cog(bot))
