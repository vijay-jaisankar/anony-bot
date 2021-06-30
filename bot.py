import discord
from discord.ext import commands
import random
import requests
from datetime import date


import keys


client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print("Anony Bot is ready")

@client.event
async def on_message(message):
    if not message.guild:
        channel = client.get_channel(keys.channel_id)
        await channel.send(message.content)


client.run(keys.botToken)
