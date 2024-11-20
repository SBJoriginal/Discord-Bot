import discord
from discord import app_commands
import os

tree = None
server_name = os.getenv("SERVER_NAME")

# Music Commands
async def setup(bot):
    global tree
    tree = bot.tree

    # Music Commands
    @tree.command(name="top_tracks", description="Get the top tracks of a user")
    @app_commands.describe(user="The user to fetch top tracks for")
    async def top_tracks_command(interaction: discord.Interaction, user: str):
        await interaction.response.send_message(f"Fetching top tracks for {user}... 🎵")

    @tree.command(name="recent_tracks", description="Get recently played tracks of a user")
    @app_commands.describe(user="The user to fetch recent tracks for")
    async def recent_tracks_command(interaction: discord.Interaction, user: str):
        await interaction.response.send_message(f"Fetching recent tracks for {user}... 🎶")

    @tree.command(name="top_artists", description="Get the top artists of a user")
    @app_commands.describe(user="The user to fetch top artists for")
    async def top_artists_command(interaction: discord.Interaction, user: str):
        await interaction.response.send_message(f"Fetching top artists for {user}... 🎤")

    @tree.command(name="track_info", description="Get information about a specific track")
    @app_commands.describe(track="The name of the track")
    async def track_info_command(interaction: discord.Interaction, track: str):
        await interaction.response.send_message(f"Fetching info for track: {track} 🎵")

    # Server Management Commands
    @tree.command(name="purge", description="Delete a specified number of messages")
    @app_commands.describe(amount="Number of messages to delete")
    async def purge_command(interaction: discord.Interaction, amount: int):
        await interaction.response.send_message(f"Purging {amount} messages... 🧹")

    @tree.command(name="ban", description="Ban a user from the server")
    @app_commands.describe(user="The user to ban")
    async def ban_command(interaction: discord.Interaction, user: str):
        await interaction.response.send_message(f"Banning user: {user} 🚫")

    @tree.command(name="kick", description="Kick a user from the server")
    @app_commands.describe(user="The user to kick")
    async def kick_command(interaction: discord.Interaction, user: str):
        await interaction.response.send_message(f"Kicking user: {user} 👢")

    @tree.command(name="roles", description="Assign or remove roles for a user")
    @app_commands.describe(user="The user to assign/remove roles for")
    async def roles_command(interaction: discord.Interaction, user: str):
        await interaction.response.send_message(f"Managing roles for {user}... 🔧")

    # Fun and Engagement Commands
    @tree.command(name="rps", description="Play a game of Rock-Paper-Scissors")
    async def rps_command(interaction: discord.Interaction):
        await interaction.response.send_message("Playing Rock-Paper-Scissors... ✂️📄✊")

    @tree.command(name="meme", description="Fetch a random meme")
    async def meme_command(interaction: discord.Interaction):
        await interaction.response.send_message("Fetching a random meme... 😂")

    @tree.command(name="gif", description="Fetch a GIF based on a keyword")
    @app_commands.describe(keyword="The keyword for the GIF")
    async def gif_command(interaction: discord.Interaction, keyword: str):
        await interaction.response.send_message(f"Fetching a GIF for: {keyword} 🎥")

    @tree.command(name="trivia", description="Start a trivia quiz game")
    async def trivia_command(interaction: discord.Interaction):
        await interaction.response.send_message("Starting a trivia game... 🧠")

    # Advanced ChatGPT Commands
    @tree.command(name="ask", description="Ask ChatGPT a question")
    @app_commands.describe(prompt="Your question or prompt")
    async def ask_command(interaction: discord.Interaction, prompt: str):
        await interaction.response.send_message(f"Asking ChatGPT: {prompt} 🤖")

    @tree.command(name="summary", description="Summarize a long message or article")
    @app_commands.describe(content="The text to summarize")
    async def summary_command(interaction: discord.Interaction, content: str):
        await interaction.response.send_message("Summarizing the content... 📜")

    @tree.command(name="translate", description="Translate text between languages")
    @app_commands.describe(text="The text to translate", language="The target language")
    async def translate_command(interaction: discord.Interaction, text: str, language: str):
        await interaction.response.send_message(f"Translating '{text}' to {language}... 🌐")

    @tree.command(name="define", description="Get definitions for words or terms")
    @app_commands.describe(term="The term to define")
    async def define_command(interaction: discord.Interaction, term: str):
        await interaction.response.send_message(f"Fetching definition for: {term} 📖")

    # Automation and Information Commands
    @tree.command(name="remind", description="Set a reminder")
    @app_commands.describe(time="When to remind", message="The reminder message")
    async def remind_command(interaction: discord.Interaction, time: str, message: str):
        await interaction.response.send_message(f"Setting a reminder: {message} at {time} ⏰")

    @tree.command(name="weather", description="Fetch current weather for a location")
    @app_commands.describe(location="The location to fetch weather for")
    async def weather_command(interaction: discord.Interaction, location: str):
        await interaction.response.send_message(f"Fetching weather for {location}... 🌦️")

    @tree.command(name="server_info", description="Get server statistics")
    async def server_info_command(interaction: discord.Interaction):
        print("Getting server info!")
        # Ensure the command is executed in a server
        if not interaction.guild:
            await interaction.response.send_message("This command can only be used in a server!")
            return

        # Acknowledge the interaction first to prevent timeout
        await interaction.response.defer(ephemeral=True)  # Acknowledge the interaction. Remove ephemeral=True so that everyone can see the message!!!!!!

        # Fetch members from the guild and exclude bots
        members = []
        async for member in interaction.guild.fetch_members():
            if not member.bot:  # Exclude bots
                members.append(member)

        response = f"""
        📊 **Server Information**
        -------------------------
        - Server Name: {interaction.guild.name}
        - Members ({len(members)}):
        """
        
        response += "\n\nAdditional Info: Coming soon!"

        # Send the response (truncate if too long)
        await interaction.followup.send(response[:2000])  # Use followup to send the actual message
        print ("server info sent!")


    @tree.command(name="server_members", description="Get all members in a server")
    async def server_members_command(interaction: discord.Interaction):
        print("Getting member info!")
        # Ensure the command is executed in a server
        if not interaction.guild:
            await interaction.response.send_message("This command can only be used in a server!")
            return

        # Acknowledge the interaction first to prevent timeout
        await interaction.response.defer(ephemeral=True)  # Acknowledge the interaction. Remove ephemeral=True so that everyone can see the message!!!!!!

        # Fetch members from the guild and exclude bots
        members = []
        async for member in interaction.guild.fetch_members():
            if not member.bot:  # Exclude bots
                members.append(member)

        # Collect member names and fetch additional profile info
        member_profiles = []
        for member in members:
            # Fetch member profile using their ID
            full_member = await interaction.guild.fetch_member(member.id)
            
            # Prepare the profile info
            profile_info = f"""
            **Name**: {full_member.global_name}"""
          # **Id**: {full_member.id} Could be added if you want or need

            member_profiles.append(profile_info)

        response = f"""
        📊 **Server Members Information**
        -------------------------
        - Server Name: {interaction.guild.name}
        - Members ({len(members)}):
        """
        response += "\n".join(member_profiles)
        response += "\n\nAdditional Info: Coming soon!"

        # Send the response (truncate if too long)
        await interaction.followup.send(response[:2000])  # Use followup to send the actual message
        print ("member info sent!")

    @tree.command(name="user_info", description="Get information about a user")
    @app_commands.describe(user="The user to fetch information for")
    async def user_info_command(interaction: discord.Interaction, user: str):
        await interaction.response.send_message(f"Fetching info for user: {user} 🔍")