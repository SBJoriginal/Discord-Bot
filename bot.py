import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from chatgpt import handle_chatgpt_response
from statfm import handle_music_command
from startup_message import opening_message

# Load environment variables
load_dotenv()

# Set up Discord bot
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(f'Bots Application ID: {bot.user.id}')

    SERVER_NAME = os.getenv("SERVER_NAME")
    CHANNEL_NAME = os.getenv("CHANNEL_NAME")
    
    # Get the guild (server) by name
    guild = discord.utils.get(bot.guilds, name=SERVER_NAME)
    if guild:
        print(f"Connected to the server: '{SERVER_NAME}'")
        
        # Get the channel by name
        channel = discord.utils.get(guild.text_channels, name=CHANNEL_NAME)
        #if channel:
            #await opening_message(channel)  # Pass the channel to the opening_message function
        #else:
            #print(f"Could not find the channel with the name '{CHANNEL_NAME}'.")
    else:
        print(f"Could not find the server with the name '{SERVER_NAME}'.")

@bot.event
async def on_message(message):
    # Prevent bot from responding to itself
    if message.author == bot.user:
        return

    # Handle ChatGPT-related responses when the bot is mentioned
    if bot.user.mentioned_in(message):
        await handle_chatgpt_response(bot, message)  # Use the function from chatgpt.py

    # Handle Stat.fm-related responses when music is mentioned
    if message.content.lower() == "music":
        await handle_music_command(bot, message)  # Use the function from statfm.py

    # Process other bot commands
    await bot.process_commands(message)

# Run the bot with your Discord token
bot.run(os.getenv('DISCORD_TOKEN'))
