# bot.py

import discord

from discord.ext import commands

token = '###'

bot = discord.Client()

file = open("words.txt", "r").read().split('\n')

# connection
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    cnt = 0
    tot = len(message.content.split())
    for word in file:
        if word in message.content:
            cnt += 1
    if ((cnt/tot) >= 0.2) & (tot >= 3):
        await message.channel.send("Jesse, what the fuck are you talking about")

# run
bot.run(token)