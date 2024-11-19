This repository contains the code for a Discord bot hosted on an AWS EC2 instance. The bot integrates with ChatGPT for conversational AI and Stat.fm for music-related commands. It is designed to run 24/7 in the cloud, providing reliable service and advanced functionality.

## Features

- **ChatGPT Integration**: The bot leverages OpenAI's GPT-3.5-turbo to respond intelligently to user queries. It can provide answers, engage in conversations, and assist users based on a defined context.
- **Stat.fm Music Integration**: Fetches music-related data, such as a user's top tracks, and provides rich responses.
- **Slash Commands**: Includes modern slash commands, such as `/top_tracks`, for user-friendly interactions.
- **Custom Startup Message**: Sends an introductory message to a specified channel upon connecting.
- **Cloud Hosting**: Hosted on AWS EC2, ensuring continuous availability and easy remote management.

## Requirements

- **Python 3.x**
- **Dependencies**: Install using the following command:
  ```bash
  pip install -r requirements.txt
  ```

## Environment Setup

Create a `.env` file in the root directory with the following variables:

```env
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
SERVER_NAME=your_server_name
CHANNEL_NAME=your_channel_name
DISCORD_GUILD_ID=your_guild_id
DISCORD_APPLICATION_ID=your_application_id
```

## Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/discord-bot.git
   cd discord-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```

## Hosting on AWS EC2

### Initial Setup

1. **SSH into the EC2 Instance**:
   ```bash
   ssh -i "path_to_your_key.pem" ec2-user@your_instance_url
   ```
2. **Navigate to the Bot Directory**:
   ```bash
   cd Discord-Bot
   ```
3. **Start the Bot**:
   ```bash
   nohup python3 bot.py &
   ```

### Updating the Bot

1. **Stop the Running Bot**:
   ```bash
   pkill -f "python3 bot.py"
   ```
2. **Upload New Files**:
   Use `scp` to transfer updated files to the EC2 instance:
   ```bash
   scp -i "path_to_your_key.pem" file_path ec2-user@your_instance_url:/home/ec2-user/Discord-Bot/
   ```
3. **Restart the Bot**:
   ```bash
   nohup python3 bot.py &
   ```

## Commands

- **ChatGPT Commands**: The bot responds to messages where it is mentioned.
- **Stat.fm Music Commands**: `/top_tracks` fetches a user's top tracks.

## File Structure

```
.
├── bot.py                 # Main bot script
├── chatgpt.py             # ChatGPT integration
├── statfm.py              # Stat.fm music command handling
├── startup_message.py     # Sends a startup message
├── requirements.txt       # Dependencies
├── .env                   # Environment variables
```