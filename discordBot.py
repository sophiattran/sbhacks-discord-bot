import discord
import os
import requests
import json
token = 'OTM5NjkwMzM3NTYyMTQ0ODc5.Yf8g0w._q2K2sBp9IlApHn1sADwnEUjbyI' # insert token here!!
client = discord.Client()
dog_words = ["dog","facts","woof","puppy","dogpics"]
programming_words = ["programming","coding","computer science","computer","visual studio","code","program","cs"]
joke_words = ["joke","funny","laugh","lol","lmao","haha"]
pun_words = ["pun","cheese","cheesy"]

headers = {
    'authorization': "GoPCfZ5gEUKf",
    'x-rapidapi-host': "random-stuff-api.p.rapidapi.com",
    'x-rapidapi-key': "e07107b648msh201d57879878f79p1547f9jsn980b64e03fa9"
    }

def get_programming_joke():
    response = requests.request("GET", 'https://random-stuff-api.p.rapidapi.com/joke', headers=headers, params={"type":"programming","blacklist":"nsfw"})
    json_data = json.loads(response.text)
    if("joke" in json_data):
        programming_joke = json_data["joke"]
    elif("setup" in json_data):
        programming_joke = json_data["setup"] + " " + json_data["delivery"]
    return(programming_joke)

def get_normal_joke():
    response = requests.request("GET", 'https://random-stuff-api.p.rapidapi.com/joke', headers=headers, params={"type":"misc","blacklist":"nsfw"})
    json_data = json.loads(response.text)
    if("joke" in json_data):
        normal_joke = json_data["joke"]
    elif("setup" in json_data):
        normal_joke = json_data["setup"] + " " + json_data["delivery"]
    return(normal_joke)

def get_pun():
    response = requests.request("GET", 'https://random-stuff-api.p.rapidapi.com/joke', headers=headers, params={"type":"pun","blacklist":"nsfw"})
    json_data = json.loads(response.text)
    if("joke" in json_data):
        pun = json_data["joke"]
    elif("setup" in json_data):
        pun = json_data["setup"] + " " + json_data["delivery"]
    return(pun)

def get_dog_fact():
    response = requests.get("https://dog-api.kinduff.com/api/facts")
    json_data = json.loads(response.text)
    dog_fact = json_data['facts'][0]
    return(dog_fact)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if message.author == client.user:
        return

    if any(word in message.content for word in dog_words):
        dog_fact = get_dog_fact()
        await message.channel.send(dog_fact)

    if any(word in message.content for word in programming_words):
        programming_joke = get_programming_joke()
        await message.channel.send(programming_joke)

    if any(word in message.content for word in joke_words):
        joke = get_normal_joke()
        await message.channel.send(joke)

    if any(word in message.content for word in pun_words):
        pun = get_pun()
        await message.channel.send(pun)

client.run(token)
