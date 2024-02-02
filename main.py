import discord  # discord.py package
import responses


async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    if channel:
        await channel.send(f"Welcome {member.mention} to the server!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: '{user_message}' ({channel})")

    if user_message and user_message[0] == '!':
        user_message = user_message[1:]
        await send_message(message, user_message)


client.run('TOKEN')
