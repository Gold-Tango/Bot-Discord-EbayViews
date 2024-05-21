import discord 

import requests 

token = 'Discord bot token'

intents = discord.Intents.default()
intents.messages = True  # Enable the bot to receive messages

# Initialize the Client with the defined intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # !views nomber_of_views link
    if message.author == client.user:
        return

    if 'hello' in message.content:
        response = 'hi'
        await message.channel.send(response)

    if '!views' in message.content:
        number_of_views = message.content.split(' ')[1]
        link = message.content.split(' ')[2]
        response = f'Adding {number_of_views} views...'
        await message.channel.send(response)

        for i in range(int(number_of_views)):
            requests.get(link)
        
        response = f'Adding {number_of_views} views.'
        await message.channel.send(response)

client.run(token)
