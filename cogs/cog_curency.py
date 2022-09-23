import asyncio
import discord
from discord.ext import tasks, commands
from requests import get
import requests


class Currencies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("CURENCIES loaded")

    @commands.command(aliases=['ETH', 'Eth', 'ethereum'])
    async def eth(self, ctx):
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h"
        response = requests.get(url)
        data = response.json()
        embed = discord.Embed(
            title='ETH', color=discord.Color.green())
        embed.add_field(name='aktualna cena',
                        value=f"{data[0]['current_price']}$")
        embed.add_field(name='min w 24h', value=f"{data[0]['low_24h']}$")
        embed.add_field(name='max w 24h', value=f"{data[0]['high_24h']}$")
        embed.add_field(name='zmiana w 24h',
                        value=data[0]['price_change_percentage_24h'])
        await ctx.message.delete()
        await ctx.channel.typing()
        await asyncio.sleep(2)
        await ctx.channel.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Currencies(bot))
