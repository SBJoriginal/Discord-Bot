import discord
from discord.ext import commands
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set server and channel names as variables
SERVER_NAME = "one of us is irrelevant"
CHANNEL_NAME = "bot_commands"

# Set up Discord bot
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    guild = discord.utils.get(bot.guilds, name=SERVER_NAME)
    if guild:
        general_channel = discord.utils.get(guild.text_channels, name=CHANNEL_NAME)
        if general_channel:
            await general_channel.send('I am alive and ready to chat!')
            print(f"Message sent to '{CHANNEL_NAME}' channel in '{SERVER_NAME}'.")
        else:
            print(f"Could not find the '{CHANNEL_NAME}' channel in '{SERVER_NAME}'.")
    else:
        print(f"Could not find the server with the name '{SERVER_NAME}'.")

# Function to get ChatGPT response using the new API method
async def get_chatgpt_response(prompt):
    print(f"Generating response for prompt: {prompt}")

    try:
        # Using the newer completions.create method for OpenAI API >= 1.0.0
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            prompt=prompt,
            max_tokens=150,  # Limit tokens to keep responses short
            temperature=0.7  # Adjust temperature for more creative responses
        )
        print("Response received from OpenAI.")
        return response.choices[0].text.strip()  # Correct access for completion response
    except Exception as e:
        print(f"Error during API call: {e}")
        return "Sorry, I couldn't process that request."

# Respond to messages with ChatGPT
@bot.event
async def on_message(message):
    # Prevent bot from responding to itself
    if message.author == bot.user:
        return

    # Check if the message mentions the bot or starts with a command prefix
    if bot.user.mentioned_in(message) or message.content.startswith("!"):
        print(f"Received message: {message.content}")
        prompt = message.content
        try:
            response = await get_chatgpt_response(prompt)
            await message.channel.send(response)
            print(f"Sent response: {response}")
        except Exception as e:
            print(f"Error processing message: {e}")
            await message.channel.send("Sorry, I couldn't process that.")
            print("Error sent to user.")

    # Process commands if needed
    await bot.process_commands(message)

# Run the bot with your Discord token
bot.run(os.getenv('DISCORD_TOKEN'))
