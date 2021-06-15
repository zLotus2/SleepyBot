import discord
import os
 
client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('>help'):
     await message.channel.send('This bot is currently in development by SleepySpeller#0289 . If you see any bugs report them to SleepySpeller#0289 Currently available commands: >help >hello >owner')
  
  if message.content.startswith('>hello'):
     await message.channel.send('Hello! My name is SleepyBot. Nice to meet you!')
     
  if message.content.startswith('>owner'):
    await message.channel.send('This bot is made by SleepySpeller#0289. GitHub page comming soon. ')

client.run('TOKEN')