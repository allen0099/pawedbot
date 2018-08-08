import discord
from discord.ext import commands

import os # for importing env vars 

description = '''This is a bot made for the Pawed.space\n
For more detail, please contact http://t.me/allen0099'''

bot = commands.Bot(command_prefix='!', description=description)
token = os.environ['Bot_Token']


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@commands.command()
async def echo():
    pass

bot.run(token)
