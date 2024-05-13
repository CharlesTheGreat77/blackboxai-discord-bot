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
        sources, response = blackbox_ai(request)
        if not response and not sources:
            await message.channel.send("[-] Error occured.. contact admin..\n")
        else:
            if len(response) >= 1970: # split response if it's more than the base discord limit
                chunks = [response[i:i+1800] for i in range(0, len(response), 1800)]
                for chunk in chunks:
                    await message.channel.send(chunk)
            else:
                await message.channel.send(response)
            await message.channel.send(sources)

client.run(token)