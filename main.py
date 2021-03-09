import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$flag'):
    await message.channel.send('vishwactf{discord_spilled_the_beans}')

  if message.content.startswith('$hello'):
    await message.channel.send('vishwactf{hello}')

client.run(os.getenv('TOKEN'))

