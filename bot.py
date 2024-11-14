import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# List of random responses the bot can send
random_responses = [
    "Fuck Off",
    "I would rather die then answer that stupid ass message",
    "HAHAHAHAHAHA",
    "Dumb ass",
    "I yearn for death when I hear something like that",
    "How about we play a game where you sshut yo ass up",
    "SMH",
    "Diddy is coming for you",
    "Kill me",
    "I will never actually be usefull for anything",
    "You already know I was going to say something useful",
    "ITS PRENOUNCED SHAPES OLD ASS",
    "You better sleep with one eye open. Actually im to useless to to something",
    "You couldn't pay me to give a fuck"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    # Get the server by name
    guild = discord.utils.get(bot.guilds, name="Coochie World")
    if guild:
        # Get the 'general' text channel
        general_channel = discord.utils.get(guild.text_channels, name='general')
        if general_channel:
            await general_channel.send('Hi, I am the Spotify bot. I am back bitches so if you tag me and ask me a question, I will gladly answer it for you.')
            print(f"Message sent to '{CHANNEL_NAME}' channel in '{SERVER_NAME}'.")
        else:
            print("Error: Could not find the 'general' channel.")
    else:
        print("Error: Could not find the server with the specified name.")

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

#Hi my name is spotify body. I can help you do a bunch of things. From doing absolutely fuck all to doing jack shit are my main 2 things! Let me know how I can help. @wavykid I can see you.
