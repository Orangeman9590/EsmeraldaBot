import random
import discord
import asyncio


responses= ['Yes', 'No', 'Highly Likely', 'Maybe', 'Not likely', 'My sources say no', 'The higher power says yes',
            'Probably', 'Probably not','Clearly', 'Very far from yes',
            'Thanks for the coin, but no', 'Yummy coin, and the answer is yes', 'Hmmmm, Yes', 'My crystal ball says no']


TOKEN = ''

client = discord.Client()

question= ''

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.hello'):
        await message.channel.send('Hello, I am Esmeralda, I have the answer to your every yes or no question')

    if message.content.startswith('.coin '):
        await message.channel.send(random.choice(responses))
        return

    if message.content.startswith('.coin'):
        await message.channel.send('What is the question?')

    if message.content.startswith('.help'):
        await message.channel.send('Type .coin and a YES or NO question and I will answer it')


@client.event
async def on_ready():
    print('RUNNING')



client.run(TOKEN)
