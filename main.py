import discord  # discord.py package
import aiohttp  # vajalik hilisemaks


# Funktsioon, mis hakkab kasutajate sõnumeid käsitlema
async def handle_response(message) -> str:
    # Teeme iga sõnumi väiketäheliseks, et endal oleks kergem
    message = message.lower()

    # Kui sõnum oli !abi, saadame kasutajale vastuse
    if message == "abi":
        return "Vastus, mille bot discordi saadab"


# Sõnumi saatmine kasutajale (siin ei pea midagi muutma)
async def send_message(message, user_message):
    try:
        response = await handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

# Boti registreerimine
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


# Tegevus, kui bot valmis laeb
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Tegevus, kui keegi serveriga liitub
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    if channel:
        await channel.send(f"Welcome {member.mention} to the server!")


# Tegevus, kui keegi serveris sõnumi saadab
@client.event
async def on_message(message):
    # Ignoreerime boti enda sõnumeid
    if message.author == client.user:
        return

    # Võtame sõnumi detailid muutujatesse
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    # Prindime enda jaoks PyCharmis iga saadetud sõnumi
    print(f"{username} said: '{user_message}' ({channel})")

    # Kui sõnum eksisteerib ja algab !-ga, hakkame seda töötlema
    if user_message and user_message[0] == '!':
        user_message = user_message[1:]
        await send_message(message, user_message)


# Paneme boti oma tokeniga tööle
client.run('TOKEN')  # <- siinne token enda omaga ära muuta!
