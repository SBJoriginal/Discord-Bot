# Discord Bot

This is a simple Discord bot that triggers the `/profile` command in the general chat.

## Requirements

- Python 3.x
- Install dependencies using `pip install -r requirements.txt`

## Setup

1. Create a `.env` file with your **DISCORD_TOKEN**.
2. Run the bot locally:
   ```bash
   python bot.py

## Running and Restarting the Bot on EC2

### Reconnect to the EC2 Instance

1. **Open PowerShell or Terminal** on your local machine.
2. **Reconnect to your EC2 instance** by running the following command:

   ```bash
   ssh -i "C:\Users\Lenny\Downloads\Discord_Bot.pem" ec2-user@ec2-107-20-116-170.compute-1.amazonaws.com
3. **Navigate to Directory**
   cd Discord-Bot
4. **Stop Running Bot (If Needed)**
   pkill -f "python3 bot.py"
5. **Start the script**
   nohup python3 bot.py &


### Saving Changes to the EC2 Instance

1. **Stop Running Bot**
   pkill -f "python3 bot.py"
2. **Save specific File in PS C:\Users\Lenny>**
   scp -i "C:\Users\Lenny\Downloads\Discord_Bot.pem" "C:\Users\Lenny\OneDrive\Desktop\Projects\Discord-Bot\bot.py" "C:\Users\Lenny\OneDrive\Desktop\Projects\Discord-Bot\requirements.txt" "C:\Users\Lenny\OneDrive\Desktop\Projects\Discord-Bot\startup_message.py" "C:\Users\Lenny\OneDrive\Desktop\Projects\Discord-Bot\chatgpt.py" "C:\Users\Lenny\OneDrive\Desktop\Projects\Discord-Bot\.env" ec2-user@ec2-107-20-116-170.compute-1.amazonaws.com:/home/ec2-user/Discord-Bot/

3. **Start the script**
   nohup python3 bot.py &