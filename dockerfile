# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make the container listen on port 8080 (optional for web apps)
EXPOSE 8080

# Define environment variable for the bot token
ENV DISCORD_TOKEN=your_discord_bot_token_here

# Run bot.py when the container starts
CMD ["python", "bot.py"]
