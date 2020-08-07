# Import required libraries

import discord
from discord.ext import commands
import config

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready!\n')

client.run(config.token)