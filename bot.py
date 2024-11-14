import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

# Set up intents and bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# List of random responses the bot can send
random_responses = [
    "yes",
    "no",
    "maybe",
    "I'm not sure",
    "ask again later"
]

# Set your server and channel name
SERVER_NAME = "one of us is irrelevant"
CHANNEL_NAME = "bot_commands"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    # Get the server by name
    guild = discord.utils.get(bot.guilds, name=SERVER_NAME)
    if guild:
        # Get the specified text channel
        general_channel = discord.utils.get(guild.text_channels, name=CHANNEL_NAME)
        if general_channel:
            await general_channel.send('Hi, I am the Spotify bot. I am back! Tag me with a question and I will answer.')
            print(f"Message sent to '{CHANNEL_NAME}' channel in '{SERVER_NAME}'.")
        else:
            print(f"Error: Could not find the channel '{CHANNEL_NAME}'.")
    else:
        print(f"Error: Could not find the server '{SERVER_NAME}'.")

# Respond to messages with a random message from the list
@bot.event
async def on_message(message):
    # Prevent bot from responding to itself
    if message.author == bot.user:
        return

    # Check if the message mentions the bot or starts with a command prefix
    if bot.user.mentioned_in(message) or message.content.startswith("!"):
        print(f"Received message: {message.content}")

        # Respond with a random message from the list
        await message.channel.send(random.choice(random_responses))
        print("Sent response")

    # Process commands if needed
    await bot.process_commands(message)

# Run the bot with your Discord token
bot.run(os.getenv('DISCORD_TOKEN'))
