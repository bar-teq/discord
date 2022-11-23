import asyncio
import discord
from discord.ext import tasks, commands
import random


# def rand_gif(self):
#     with open("/home/carmel/discobot/links/lol.txt", "r") as f:
#         urls = f.readlines()
#         url = random.choice(urls)
#         print(url)
#         print("jeden")
#     return url


class Onmsg_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LISTENER loaded")

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        role = discord.utils.get(after.guild.roles, name="LA player")
        if role in before.roles:
            if str(after.status) == 'online' and str(before.status) == 'offline':
                print(after.name)
                await self.bot.get_channel(1015300311826583552).send(f"oho {after.display_name} wpadł po gzika")
                print(after.guild)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.type == discord.MessageType.reply:
            if message.content == 'dodaj':
                print(message.content)
                print(message.id)
                messageid = await message.channel.fetch_message(message.reference.message_id)
                print(messageid)
                print(message.reference.message_id)
                print('test')
                msgid = message.reference.message_id
                print('test2')
                msg = await self.bot.get_channel(1015300311826583552).fetch_message(msgid)
                # try:
                #     msg = await channel.fetch_message(msgid)
                # except NotFound:
                #     continue
                print('test3')
                print(msg.content)
                with open('/home/carmel/discobot/links/cytat.txt', 'a') as f:
                    f.write(f"{msg.content} \n")
                await message.channel.send('cytat dodany')

        # if message.content.startswith('.'):
        #     return

        # msgs = 0
        async def rand_gif(self, category):
            with open(f"d:/python/discord/links/{category}.txt", "r") as f:
                urls = f.readlines()
                await message.reply(random.choice(urls))
            return
        # if message.content == "lol":
        #     await rand_gif(self, 'lol')
        #     await message.delete(delay=0.5)
        # if "lol" in message.content and message.content != "lol":
        #     await rand_gif(self, 'lol')
        #     await message.add_reaction("😆")
        # if message.content == "rip":
        #     await rand_gif(self, 'rip')
        #     await message.delete(delay=0.5)
        # if "rip" in message.content and message.content != "rip":
        #     await rand_gif(self, 'rip')
        #     await message.add_reaction("😟")
        # if message.content == "papiez":
        #     await rand_gif(self, 'papiez')
        #     await message.delete(delay=0.5)
        # if "papiez" in message.content and message.content != "papiez":
        #     await rand_gif(self, 'papiez')
        #     await message.add_reaction("✝️")
        pis = ['pis', 'pisior', 'PIS']
        if any(_ in message.content.split(' ') for _ in pis):
            await rand_gif(self, 'pis')
            #
        lol = ['lol', 'haha', 'LOL']
        if any(_ in message.content.split(' ') for _ in lol):
            await rand_gif(self, 'lol')
            #
        rip = ['rip']
        if any(_ in message.content.split(' ') for _ in rip):
            await rand_gif(self, 'rip')
            #
        papiez = ['papiez', 'papaj', 'jp2']
        if any(_ in message.content.split(' ') for _ in papiez):
            await rand_gif(self, 'papiez')
            #
        tusk = ['Tusk', 'tusk', 'donald', 'tuska']
        if any(_ in message.content.split(' ') for _ in tusk):
            await rand_gif(self, 'tusk')
            #
        duda = ['duda', 'Duda', 'prezydent']
        if any(_ in message.content.split(' ') for _ in duda):
            await rand_gif(self, 'duda')
            #
        kaczynski = ['kaczor', 'kaczynski', 'jarek']
        if any(_ in message.content.split(' ') for _ in kaczynski):
            await rand_gif(self, 'kaczynski')
            #
        asmond = ['asmond', 'asmrond', 'asmon']
        if any(_ in message.content.split(' ') for _ in asmond):
            await rand_gif(self, 'asmond')
            if len(message.content.split(' ')) <= 1:
                await message.delete(delay=1)
            #
        gramy = ['gramy?']
        if any(_ in message.content.split(' ') for _ in gramy):
            await rand_gif(self, 'gramy')
            if len(message.content.split(' ')) <= 1:
                await message.delete(delay=1)
            #
        halo = ['halo', 'hallo', 'hello']
        if any(_ in message.content.split(' ') for _ in halo):
            await rand_gif(self, 'halo')
            if len(message.content.split(' ')) <= 1:
                await message.delete(delay=1)
            #
        morawiecki = ['mateusz', 'vateusz', 'morawiecki']
        if any(_ in message.content.split(' ') for _ in morawiecki):
            await rand_gif(self, 'morawiecki')
            if len(message.content.split(' ')) <= 1:
                await message.delete(delay=1)
        # if len(message.content) > 1:
        #     msgs += 1
        #     print(msgs)


async def setup(bot: commands.Bot):
    await bot.add_cog(Onmsg_cog(bot))
