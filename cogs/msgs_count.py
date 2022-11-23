import asyncio
import discord
from discord.ext import tasks, commands
import random

msgs = 0


class liczydlo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("liczydlo")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "www" in message.content:
            return
        if "gif" in message.content:
            return
        if "https" in message.content:
            return
        if len(message.content) > 5:
            if " " in message.content:
                with open('d:/python/discord/links/cytat.txt', 'a') as f:
                    f.write(f"{message.content} \n")
        global msgs
        msgs += 1
        print(message.content)
        print(msgs)
        if msgs == 6:
            print("random")
            with open("d:/python/discord/links/cytat.txt", "r") as f:
                urls = f.readlines()
            await message.channel.send(random.choice(urls))

            msgs = 0


async def setup(bot: commands.Bot):
    await bot.add_cog(liczydlo(bot))
