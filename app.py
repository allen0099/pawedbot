from discord.ext import commands
from draw import ToS, Dinner
import os

token = os.environ['Bot_Token']  # token here

description = '''This is a bot made for the Pawed.space\n
For more detail, please contact http://t.me/allen0099'''

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def meow():
    await bot.say('meow')


@bot.command()
async def draw():
    t = ToS()
    await bot.say('{}'.format(t.draw()[0]))
    
@bot.command()
async def dinner():
    await bot.say(Dinner().draw())

bot.run(token)
