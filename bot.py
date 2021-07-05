from discord.ext import commands
import keys

client = commands.Bot(command_prefix= '.')
confession_counter = 0

@client.event
async def on_ready():
    print("Anony Bot is ready")

def clean_embed(embed, counter):
    embed.title = embed.title + ' ' + str(counter)
    return embed

@client.event
async def on_message(message):
    send_channel = client.get_channel(keys.send_channel_id)
    embed = message.embeds[0]
    if (int(message.channel.id) == keys.recv_channel_id) and ('confession' in embed.title.lower()):
        global confession_counter
        confession_counter += 1
        await send_channel.send(embed=clean_embed(embed, confession_counter))


client.run(keys.botToken)
