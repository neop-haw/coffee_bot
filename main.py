# Import required libraries

import discord
from discord.ext import commands
import config
import local_data
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
		url=local_data.wlcm_img,
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

	print(f'{message.author} ({message.author.display_name}) : {message.content}')

	if message.author == client.user:
		return

	coffee = ['coffee', 'кофе']
	lst = [word.lower() for word in message.content.split(' ')]

	find = re.search(r'кофе', message.content.lower())

	if find:
		await message.channel.send(f'**КОФЕ** :coffee:')

	await client.process_commands(message)


# Commands to use (e.g. !foo [...])

@client.command(pass_context=True)
async def ping(ctx):
	"""Спросить задержку на сервере."""

	await ctx.send(f'Ваш пинг - {round(client.latency * 1000)}ms')


@client.command(alieses=['кофе', 'coffee'])
async def coffee(ctx):
	"""Объявить Кофе-тайм и позвать всех на кофе!

	Everybody have to drink at least a cup coffee!
	"""

	pass


@client.command(alieses=['пикча', 'рандом', 'random'])
async def pic(ctx):
	"""Попросить рандомную картинку."""

	f_path = random.choice(local_data.imgs_paths)
	f_name = f_path.split('/')[-1]
	image = discord.File(f_path, filename=f_name)

	rndm_embed = discord.Embed()
	rndm_embed.set_image(url=f'attachment://{f_name}')

	await ctx.channel.send(file=image, embed=rndm_embed)


# Run bot

client.run(config.token)
