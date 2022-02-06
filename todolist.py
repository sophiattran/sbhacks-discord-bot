# use api to send inspirational messages

import discord
import os
import time
token = '' # insert token here
client = discord.Client()
todolist = []


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "$help":
        await message.channel.send("here are your possible commands! $hello, $dogpics, $todo, $todo check, $todo remove, and more. hope that helps :)")

    if message.content == ('$todo'):
        await message.channel.send('correct usage: $todo [message]')
    if message.content.startswith('$todo '):
        print(message.content[6:])
        if message.content[6:] == 'check':
            printthis = 'to do list:'
            if todolist == []:
                await message.channel.send('your to do list is empty :))')
            else:
                for item in todolist:
                    printthis += '\n- ' + str(item)
                await message.channel.send(printthis)
        elif message.content[6:].startswith('remove '):
            print(message.content[13:])
            print(todolist)
            if message.content[13:] in todolist:
                todolist.remove(message.content[13:])
                await message.channel.send(message.content[13:]  + ' has been removed! yayyy good job!! :^)')
            else:
                await message.channel.send("can't remove that from your todo list! it doesn't exist :,)")
        else:
            if todolist == []:
                await message.channel.send("creating to do list")
            await message.channel.send('adding ' +  message.content[6:] + ' to your to do list!')
            todolist.append(message.content[6:])
            print(todolist)
        #await message.channel.send(message.author.mention)
        
'''
    if message.content.startswith('$remind'):
        print(time.ctime(time.time()))
        newtime = time.strptime(message.content[8:], "%B %d, %Y at %H:%M" )
        await message.channel.send('ok')
        #await message.channel.send(message.author.mention)
    if message.content.startswith('$remind'):
        print(time.ctime(time.time()))
        newtime = time.strptime(message.content[8:], "%B %d, %Y at %H:%M" )
        newtime2 = time.mktime(newtime)
        await message.channel.send('ok!')
        #await message.channel.send(message.author.mention)

# search async functions
#if time.time() >= newtime2:
    #await message.channel.send(message.author.mention)
'''


    
client.run(token)