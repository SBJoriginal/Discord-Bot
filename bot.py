import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from chatgpt import handle_chatgpt_response
from startup_message import opening_message
from commands import setup  # Import the setup function that initializes the tree


# Load environment variables
load_dotenv()

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Initialize the CommandTree after the bot is ready
@bot.event
async def on_ready():
    
    await setup(bot)

    print(f"Logged in as {bot.user}")
    print(f"Bot's Application ID: {bot.user.id}")

    SERVER_NAME = os.getenv("SERVER_NAME")
    CHANNEL_NAME = os.getenv("CHANNEL_NAME")
    
    # Get the guild (server) by name
    guild = discord.utils.get(bot.guilds, name=SERVER_NAME)
    if guild:
        print(f"Connected to the server: '{SERVER_NAME}'")
        
        # Get the channel by name
        channel = discord.utils.get(guild.text_channels, name=CHANNEL_NAME)
        if channel:
            await opening_message(channel)  # Call the opening message function here
        else:
            print(f"Could not find the channel with the name '{CHANNEL_NAME}'.")
    else:
        print(f"Could not find the server with the name '{SERVER_NAME}'.")

    # Sync slash commands
    try:
        guild_id = os.getenv("DISCORD_GUILD_ID")
        if guild_id:
            guild = discord.Object(id=int(guild_id))
            await tree.sync(guild=guild)  # Sync to specific guild
            print(f"Commands synced successfully for guild {guild.id}.")
        else:
            await tree.sync()  # Global sync
            print("Commands synced successfully globally.")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.event
async def on_message(message):
    # Prevent the bot from responding to itself
    if message.author == bot.user:
        return

    # Handle ChatGPT-related responses when the bot is mentioned
    if bot.user.mentioned_in(message):
        await handle_chatgpt_response(bot, message)

    # Process other bot commands
    await bot.process_commands(message)

# Run the bot with the token from .env
bot.run(os.getenv("DISCORD_TOKEN"))
