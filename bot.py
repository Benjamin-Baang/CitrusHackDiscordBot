# bot.py
import os
import random
import json

import discord
from dotenv import load_dotenv
from discord.ext import commands
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@bot.command(name='facts')
async def fact(ctx, animal: str):
    # cat = [
    #     'Meow!',
    # ]
    # response = random.choice(cat)
    # await ctx.send(response)
    if animal == 'cat':
        facts = json.loads(requests.get('https://cat-fact.herokuapp.com/facts').content)
        response = facts[random.randint(0, len(facts)-1)]['text']
    elif animal == 'dog':
        response = 'Woof!'
    await ctx.send(response)

bot.run(TOKEN)