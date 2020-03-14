import discord
from discord.ext import commands
import datetime

from discord.ext.commands import bot

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is Online Boi')


@client.event
async def on_member_join(member):
    a = member.created_at
    b = datetime.datetime.now()
    c = b - a
    print(f'{member} has joined a server')
    if c.days < 30:
        await member.send('Your Acc is new so it was auto kicked')
        await member.kick()



client.run('NjcwNjc3NDExMjU1NTQ5OTUy.XmxbPQ.zfLMfRfVX6Kg0wkbMvkBGYKHQ64')
