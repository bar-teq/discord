import discord
from discord.ext import tasks, commands
import requests


class Backgroundtasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.status.start()
        print('BACKGROUND TASK loaded')
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"eth ↖️"))

    @tasks.loop(seconds=60)
    async def status(self):
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h"
        response = requests.get(url)
        data = response.json()
        eth_price = data[0]['current_price']
        for guild in self.bot.guilds:
            await guild.me.edit(nick=f"{eth_price}")


# @bot.event
# async def on_ready():
#     # (name='test'))
#     guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
#     print(
#         f'{bot.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})')
#         channel = bot.get_channel(542748371912491049)
#         # await channel.send(data[0]['price_change_percentage_1h_in_currency'])
#         await asyncio.sleep(60)


async def setup(bot: commands.Bot):
    await bot.add_cog(Backgroundtasks(bot))
