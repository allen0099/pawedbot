import discord
from discord.ext import commands

description = '''This is a bot make for Pawed.space only.

For more detail, contact http://t.me/allen0099'''
bot = commands.Bot(command_prefix='!', description=description)
token = '*'


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
