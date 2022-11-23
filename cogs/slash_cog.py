import discord
from discord import app_commands
from discord.ext import commands
import requests


class slash(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("slash loaded")

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"synced {len(fmt)} commands")

    @app_commands.command(name="command", description="opis")
    async def command(self, interaction: discord.Interaction, question: str):
        await interaction.response.send_message("Hello from command 1!")

    @app_commands.command(name="eth", description="cena eth")
    async def eth(self, interaction: discord.Interaction):
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
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="papiez", description="papiezgif")
    async def papiez(self, interaction: discord.Interaction):
        await interaction.response.send_message("https://tenor.com/view/papież-papiesz-papjesz-wojtyła-jp2-gif-25296294")

    @app_commands.command(name="command-2")
    async def my_private_command(self, interaction: discord.Interaction) -> None:
        """ /command-2 """
        await interaction.response.send_message("Hello from private command!", ephemeral=True)


# async def setup(bot: commands.Bot) -> None:
#     await bot.add_cog(slash(bot), guilds=[discord.Object(id=1015296364021809233)])
