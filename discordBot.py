import discord
import requests
#import os
import space

token = '' # insert token here!!

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

# template
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# dog image feature
    if message.content.startswith('$dogpics'):
        dog_info = requests.get("https://dog.ceo/api/breeds/image/random")
        embed = discord.Embed(
            title="Dog!", description="Feeling down? Have a dog!", color=0x047C91
        )
        embed.set_image(url=dog_info.json()["message"])
        await message.channel.send(embed=embed)

# space-stuff
    if "asteroid" in message.content or "jpl" in message.content or "space" in message.content:
        await message.channel.send(space.get_asteroid_death())

    if "solar eclipse" in message.content or "solar" in message.content:
        await message.channel.send(space.get_solar_eclipse())


client.run(token)
