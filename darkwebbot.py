# Bot Configuration
TOKEN = ""
import discord
import json
import os

# Setup the client and intents
intents = discord.Intents.default()
intents.messages = True
intents.dm_messages = True
intents.typing = False
client = discord.Client(intents=intents)

# Path to your JSON database
db_path = 'db.json'

# Load the database
if os.path.exists(db_path):
    with open(db_path, 'r') as f:
        db = json.load(f)
else:
    db = {}

# Log and Message Channel IDs (Replace with your actual IDs)
LOG_CHANNEL_ID = 1234567890123
MESSAGE_CHANNEL_ID = 1234567890123

log_channel = None

def save_db():
    """Function to save the database after modifications."""
    with open(db_path, 'w') as f:
        json.dump(db, f, indent=4)

async def log_message(message, user=None):
    """Function to send logs to the log channel with detailed info."""
    if log_channel:
        embed = discord.Embed(
            title="Detailed Log Message",
            description=message,
            color=discord.Color.blurple()  
        )
        if user:
            embed.set_footer(text=f"Logged by {user.name}", icon_url=user.avatar.url)
            embed.set_thumbnail(url=user.avatar.url)  

        await log_channel.send(embed=embed)

async def send_anon_message(channel, user, message):
    """Send an anonymous message to a specified channel."""
    user_data = db.get(str(user.id))
    if user_data:
        code = user_data.get('code')
        if code:
            log_msg = f"Anon message from [{code}] ({user.mention}) - {message}"
            await log_message(log_msg, user)  

            embed = discord.Embed(
                title=f"ANON [{code}]",
                description=message,
                color=discord.Color.green()
            )
            await channel.send(embed=embed)
        else:
            await user.send("Error: Your registration is incomplete. Please register first.")
    else:
        await user.send("Error: You need to register first. Type 'register' to start.")

async def handle_registration(message):
    """Handle the user registration process."""
    if message.content.isdigit() and len(message.content) == 4:
        code_exists = any(user_data.get('code') == message.content for user_data in db.values())

        if code_exists:
            await message.author.send("This code is already taken! Please enter a different 4-digit code.")
        else:
            db[str(message.author.id)] = {'code': message.content}
            save_db()
            log_msg = f"User [{message.author}] (ID: {message.author.mention}) registered with code {message.content}"
            await log_message(log_msg, message.author)  

            embed = discord.Embed(
                title="Registration Complete",
                description=f"You are now registered with code {message.content}",
                color=discord.Color.green()
            )
            embed.set_thumbnail(url=message.author.avatar.url)  
            embed.set_footer(text=f"Welcome {message.author.name}", icon_url=message.author.avatar.url)
            await message.author.send(embed=embed)
    else:
        await message.author.send('Invalid code! Please enter a 4-digit numeric code.')

async def handle_anon_message(message):
    """Handle anonymous message posting."""
    if message.content.lower().startswith('anon ') and str(message.author.id) in db:
        channel = client.get_channel(MESSAGE_CHANNEL_ID)  
        await send_anon_message(channel, message.author, message.content[5:])  
        await message.author.send('Your anonymous message has been posted!')
    else:
        await message.author.send('You are not registered. Please type "register" to start the registration process.')

@client.event
async def on_ready():
    """This event triggers when the bot is ready."""
    global log_channel
    log_channel = client.get_channel(LOG_CHANNEL_ID)  
    if log_channel:
        print(f'Logged in as {client.user} and connected to log channel {log_channel.name}')
        await log_message(f'Bot {client.user} is now online and connected to {log_channel.name}.')

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="gangs secretly"))

@client.event
async def on_message(message):
    """This event triggers when the bot receives a message."""
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        if message.content.lower() == 'register':
            if str(message.author.id) in db:
                await message.author.send('You are already registered!')
            else:
                await message.author.send('Please enter a 4-digit numeric code to complete registration.')
                return

        if str(message.author.id) not in db and message.content.isdigit():
            await handle_registration(message)
            return

        if message.content.lower().startswith('anon '):
            await handle_anon_message(message)
        else:
            await message.author.send('Invalid command. To register, type "register". To send an anonymous message, use: "anon <message>"')

client.run(TOKEN)  # Replace with your bot's token