import discord
from discord import app_commands
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set up the Discord client and command tree
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Define the /top tracks command
@tree.command(name="top_tracks", description="Get the top tracks of a user")
@app_commands.describe(user="The user to fetch top tracks for")
async def top_tracks_command(interaction: discord.Interaction, user: str):
    # Simply respond to the command for now
    await interaction.response.send_message(f"Fetching top tracks for {user}... 🎵")

# Sync commands when the bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    try:
        await tree.sync()
        print("Commands synced successfully.")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Expose a simple function to execute the command
async def handle_music_command(bot):
    # Simulate sending the /top tracks command
    print("Executing /top tracks command.")
    # Since you can't programmatically invoke a slash command directly,
    # this placeholder ensures your structure is ready for future use.
