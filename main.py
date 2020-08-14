# Import required libraries

import discord
from discord.ext import commands
import config
import random
import re	# Seachring 'coffee'

# Sending images
# import json
# import requests


# Main bot client

client = commands.Bot(command_prefix='!')


# Events to respond to user's actions (e.g. logging in, typing)

@client.event
async def on_ready():

    print('Bot is ready!\n')


@client.event
async def on_member_join(member):
	print(f'{member} has joined a server.')

	wlcm_embed = discord.Embed(colour='0xF2E41F',
		url='https://sun9-65.userapi.com/HsRPSsFPIEVEpTTUajNunzKvhTTCL5p2nGaPTA/FtRuqIRZOfE.jpg',
		title='ДОБРО ПОЖАЛОВАТЬ!'
		)

	await member.create_dm()
	await member.dm_channel.send(
		f'```Привет, {member.name}!\nДобро пожаловать на Кофе-сервер!\nЗдесь ты можешь общаться с участниками сервера и играть с ними.\nА самое главное здесь - это КОФЕ!! Если ты любишь кофе, то этот сервер для тебя!\nЖелаем приятного развлечения и кофепития!```', embed=wlcm_embed)


@client.event
async def on_member_remove(member):

    print(f'{member} has left a server.')


@client.event
async def on_message(message):
	"""This fuction is the meaning of bot's life!"""

	if message.author == client.user:
		return

	# coffee = ['coffee', 'кофе']
	# lst = [word.lower() for word in message.content.split(' ')]
	# print(lst)

	find = re.search(r'кофе', message.content.lower())

	if find:
		await message.channel.send(f'**КОФЕ** :coffee:')


# Commands to use (e.g. !foo [...])

@client.command()
async def ping(ctx):

    await ctx.send(f'Your ping is {round(client.latency * 1000)}ms')


# @client.command(alieses=['coffee'])
# async def coffee(context, message):

#     responses = ['I want some coffee.',
#                  'Gimme coffee!',
#                  'I want more coffee!!',
#                  'Coffee?',
#                  'Let\'s have some coffee']

#     await context.send(f'{random.choice(responses)}')


@client.command(alieses=['кофе', 'coffee'])
async def coffee(ctx):
	"""Fuction activates Coffee-Time!

	Everybody have to drink at least a cup coffee!
	"""

	pass


# Run bot

client.run(config.token)
