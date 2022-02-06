import discord
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

# space-stuff
    if "asteroid" in message.content or "jpl" in message.content or "space" in message.content:
        await message.channel.send(space.get_asteroid_death())

    if "solar eclipse" in message.content or "solar" in message.content:
        await message.channel.send(space.get_solar_eclipse())


client.run(token)
