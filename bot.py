import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
<<<<<<< Updated upstream
load_dotenv()

=======
import random  # Import the random module

# Load environment variables
load_dotenv()

# Set up OpenAI API key (you may still use it later if needed)
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set server and channel names as variables
SERVER_NAME = "Coochie World"
CHANNEL_NAME = "general"

# Set up Discord bot
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            try:
                # Mention the stat.fm bot using its ID in the message
                await general_channel.send('test')
                print("Message '/profile' sent successfully.")
            except Exception as e:
                print(f"Error sending command: {e}")
=======
            await general_channel.send('Hi, I am the Spotify bot. I am back bitches so if you tag me and ask me a question, I will gladly answer it for you.')
            print(f"Message sent to '{CHANNEL_NAME}' channel in '{SERVER_NAME}'.")
>>>>>>> Stashed changes
        else:
            print("Error: Could not find the 'general' channel.")
    else:
        print("Error: Could not find the server with the specified name.")

<<<<<<< Updated upstream
=======
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
>>>>>>> Stashed changes
bot.run(os.getenv('DISCORD_TOKEN'))

#Hi my name is spotify body. I can help you do a bunch of things. From doing absolutely fuck all to doing jack shit are my main 2 things! Let me know how I can help. @wavykid I can see you.
