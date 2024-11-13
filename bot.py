import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    # Get the server by name
    guild = discord.utils.get(bot.guilds, name="Coochie World")
    if guild:
        # Get the 'general' text channel
        general_channel = discord.utils.get(guild.text_channels, name='general')
        if general_channel:
            try:
                # Mention the stat.fm bot using its ID in the message
                await general_channel.send('test')
                print("Message '/profile' sent successfully.")
            except Exception as e:
                print(f"Error sending command: {e}")
        else:
            print("Error: Could not find the 'general' channel.")
    else:
        print("Error: Could not find the server with the specified name.")

bot.run(os.getenv('DISCORD_TOKEN'))

#Hi my name is spotify body. I can help you do a bunch of things. From doing absolutely fuck all to doing jack shit are my main 2 things! Let me know how I can help. @wavykid I can see you.
