# startup_message.py
import discord

async def opening_message(channel):
    # Send a message to the specified channel
    await channel.send("I am now connected to the cloud! That means I am always available")
    print(f"Opening message sent to channel: {channel.name}")
