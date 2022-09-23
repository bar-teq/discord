import asyncio
import discord
from discord.ext import tasks, commands
import random


class Onmsg_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LISTENER loaded")

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        role = discord.utils.get(after.guild.roles, name="Member")
        if role in before.roles:
            if str(after.status) == 'online' and str(before.status) == 'offline':
                print(after.name)
                await self.bot.get_channel(993905352498221066).send(f"{after.name} 🟢")
                print(after.guild)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content == "lol":
            with open("d:/python/discord/links/lol.txt", "r") as f:
                urls = f.readlines()
            await message.channel.typing()
            await asyncio.sleep(1.5)
            await message.delete(delay=1)
            await message.channel.send(random.choice(urls))
        if "lol" in message.content and message.content != "lol":
            with open("d:/python/discord/links/lol.txt", "r") as f:
                urls = f.readlines()
            await message.channel.typing()
            await asyncio.sleep(1.5)
            await message.channel.send(random.choice(urls))
            await message.add_reaction("😆")


async def setup(bot: commands.Bot):
    await bot.add_cog(Onmsg_cog(bot))
