# Import required libraries

import discord
from discord.ext import commands
import config
import random


# Main bot client

client = commands.Bot(command_prefix='!')


# Events to respond to user's actions (e.g. logging in, typing)

@client.event
async def on_ready():

    print('Bot is ready!\n')


@client.event
async def on_member_join(member):

    print(f'{member} has joined a server.')


@client.event
async def on_member_remove(member):

    print(f'{member} has left a server.')


@client.event
async def on_message(message):
	"""This fuction is the meaning of bot's life!"""

	if message.author == client.user:
		return

	coffee = ['coffee', 'кофе']
	lst = [word.lower() for word in message.content.split(' ')]
	print(lst)
	if set(coffee) & set(lst):
		await message.channel.send('КОФЕ')



# Commands to use (e.g. !foo [...])

@client.command()
async def ping(ctx):

    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(alieses=['coffee'])
async def coffee(context, message):

    responses = ['I want some coffee.',
                 'Gimme coffee!',
                 'I want more coffee!!',
                 'Coffee?',
                 'Let\'s have some coffee']

    await context.send(f'{random.choice(responses)}')


# Run bot

client.run(config.token)
