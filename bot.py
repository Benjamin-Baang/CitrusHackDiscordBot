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
    if animal == 'cat':
        facts = json.loads(requests.get('https://cat-fact.herokuapp.com/facts').content)
        response = facts[random.randint(0, len(facts)-1)]['text']
    elif animal == 'dog':
        facts = json.loads(requests.get('https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1').content)
        response = facts[0]['fact']
    await ctx.send(response)

@bot.command(name='pics')
async def fact(ctx, animal: str):
    if animal == 'cat':
        image = 'images/cats/' + str(random.randint(1,5)) + '.png'
        response = discord.File(image)
    elif animal == 'dog':
        image = 'images/dogs/' + str(random.randint(1,7)) + '.png'
        response = discord.File(image)
    await ctx.send(file=response)

bot.run(TOKEN)