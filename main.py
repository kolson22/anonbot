import discord
import os

TOKEN = os.getenv("TOKEN")

client = discord.Client(intents=discord.Intents().all())

@client.event
async def on_ready():
  print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
  if "Direct Message" in str(message.channel):
    channel = client.get_channel(382984951731060767)
    await channel.send(message.content)

client.run(TOKEN)