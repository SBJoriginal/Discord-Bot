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
        # Using the newer chat-based API method for GPT models (like GPT-3.5 and GPT-4)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,  # Limit tokens to keep responses short
            temperature=0.7  # Adjust temperature for more creative responses
        )
        print("Response received from OpenAI.")
        return response['choices'][0]['message']['content'].strip()  # Correct access for chat-based response
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
        context = "This is your context: My name is Spotify Bot. My duty is to answer any questions related to Coochie World, providing accurate and helpful information. When prompted, I will respond in under 150 tokens."
        prompt_with_context = context + prompt
        try:
            response = await get_chatgpt_response(prompt_with_context)
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
