import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents,)


@bot.event
async def on_ready():
    print('BOT ONLINE')


async def load():
    for file in os.listdir('d:/python/discord/cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')


async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())
