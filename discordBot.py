import discord
import os
import requests
import json
import space
import random

token = 'OTM5NjkwMzM3NTYyMTQ0ODc5.Yf8g0w.w5JGOEvAzxjcRyFqVwhi-vM8YIs' # insert token here!!
client = discord.Client()
dog_words = ["dog","facts","woof","puppy","dogpics"]
programming_words = ["programming","coding","computer science","computer","visual studio","code","program"]
greetings = ["hi! hope ur doing well homie","hey bestie!","what's up mate","hii omg i've missed you","heyy!!","hello!!"]
laugh_words = ["lol","lmao","lmfao","haha","hehe","lul","xd","rofl",":joy:","LOL","LMAO","LMFAO","HAHA","HEHE","LUL","XD","ROFL"]
todolist = []
users = []

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
    dog_fact = "Did you know? " + json_data['facts'][0]
    return(dog_fact)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

# greeting feature
    if message.content.startswith('$hi') or message.content.startswith('$hello'):
        await message.channel.send(random.choice(greetings))

# laughs along 
    if any(word in message.content for word in laugh_words):
        await message.channel.send(random.choice(laugh_words))

# dog facts
    if any('$' + word in message.content for word in dog_words):
        dog_fact = get_dog_fact()
        await message.channel.send(dog_fact)

# jokes
    if any('$' + word in message.content for word in programming_words):
        programming_joke = get_programming_joke()
        await message.channel.send(programming_joke)

    if "$joke" in message.content:
        joke = get_normal_joke()
        await message.channel.send(joke)

    if "$pun" in message.content:
        pun = get_pun()
        await message.channel.send(pun)

# dog image feature
    if message.content.startswith('$dogpics'):
        dog_info = requests.get("https://dog.ceo/api/breeds/image/random")
        embed = discord.Embed(
            title="Dog!", description="Feeling down? Have a dog!", color=0x047C91
        )
        embed.set_image(url=dog_info.json()["message"])
        await message.channel.send(embed=embed)

# space-stuff
    if "$asteroid" in message.content or "$jpl" in message.content or "$space" in message.content:
        await message.channel.send(space.get_asteroid_death())

    if "$eclipse" in message.content or "$solar" in message.content:
        await message.channel.send(space.get_solar_eclipse())
        
# to do list
    if message.content == "$help":
        await message.channel.send("here are your possible commands! $hello, $dogpics, $todo, $todo check, $todo remove, and more. hope that helps :)")

    if message.content == ('$todo'):
        await message.channel.send('correct usage: $todo [message], $todo check, $todo remove [message]')
    if message.content.startswith('$todo '):
        if message.content[6:] == 'check':
            printthis = 'to do list:'
            if message.author not in users:
                await message.channel.send('your to do list is empty :))')
            else:
                for item in users[users.index(message.author)+1]:
                    printthis += '\n- ' + str(item)
                await message.channel.send(printthis)
        elif message.content[6:].startswith('remove '):
            todolist = users[users.index(message.author)+1]
            if message.content[13:] in todolist:
                todolist.remove(message.content[13:])
                await message.channel.send(message.content[13:]  + ' has been removed! yayyy good job!! :^)')
                if todolist == []:
                    users.remove(users.index(message.author)+1)
                    users.remove(users.index(message.author))
            else:
                await message.channel.send("can't remove that from your todo list! it doesn't exist :,)")
        else:
            if message.author not in users:
                await message.channel.send("creating new to do list for " + str(message.author) + "!")
                users.append(message.author) 
                users.append([]) 
            await message.channel.send('adding ' +  message.content[6:] + ' to your to do list!')
            todolist = users[users.index(message.author)+1]
            todolist.append(message.content[6:])


client.run(token)
