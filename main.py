import discord
import io, base64, os
from stablediff import Stable

TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")
STEPS = os.getenv("STEPS")

client = discord.Client(intents=discord.Intents().all())

@client.event
async def on_ready():
  print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
  if "Direct Message" in str(message.channel):
    channel = client.get_channel(382984951731060767)
    stable = Stable(URL, steps=STEPS)
    images = stable.create_image(message.content)
    # files = [discord.File(io.BytesIO(base64.b64decode(image))) for image in images]
    file = discord.File(io.BytesIO(base64.b64decode(images[0])), filename="image0.png")
    embed = discord.Embed()
    embed.set_image(url="attachment://image0.png")
    await channel.send(file=file, embed=embed)

client.run(TOKEN)