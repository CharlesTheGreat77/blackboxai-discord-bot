from core.ai import blackbox_ai
import discord

token = '' # I would advice safer ways of importing ones token.. but for simplicity 
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!blackbox'): # change as necessary
        request = message.content.replace('!blackbox ', '')
        response = blackbox_ai(request)
        if len(response) >= 1970: # split response if it's more than the base discord limit
            for line in response.split():
                await message.channel.send(line)
        else:
            await message.channel.send(response)

client.run(token)