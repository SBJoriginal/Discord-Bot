import discord
from discord import app_commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the Discord Application ID from environment variables
DISCORD_APPLICATION_ID = os.getenv("DISCORD_APPLICATION_ID")

# Set up the tree (this doesn't need to be in statfm.py, but for now we'll leave it here)
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Function to handle the /top tracks command for music
async def handle_music_command(bot, message):
    try:
        # Log the message and guild details
        print(f"Received message: {message.content} from {message.author} in guild {message.guild.name} ({message.guild.id})")

        # Extract guild ID from the bot's server
        guild_id = message.guild.id
        user_mention = "@sbjoriginal"  # Static user mention for top tracks. Adjust as needed.

        # Sync the commands to Discord (only needs to be done once at startup)
        print(f"Syncing commands to guild {guild_id}...")
        await tree.sync(guild=discord.Object(id=guild_id))
        print(f"Commands synced for guild {guild_id}")

        # Get the '/top tracks' command
        command = tree.get_command("top tracks")
        if command:
            print("Command '/top tracks' found, invoking...")

            # Create the interaction and invoke the slash command
            await command.invoke(
                discord.Interaction(
                    client=bot,
                    guild=discord.Object(id=guild_id),
                    user=message.author,
                    data={
                        "name": "top tracks",
                        "options": [{"name": "user", "value": user_mention}]
                    }
                )
            )
            print(f"Executed '/top tracks' command in guild {guild_id}")
        else:
            print(f"Command '/top tracks' not found in guild {guild_id}")
            await message.channel.send("❌ Command '/top tracks' not found.")
    except Exception as e:
        # Log any error encountered
        print(f"Error executing music command: {e}")
        await message.channel.send(f"❌ There was an error executing the music command: {e}")
