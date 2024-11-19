import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

async def get_chatgpt_response(prompt: str) -> str:

    print(f"Generating response for prompt: {prompt}")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        print("Response received from OpenAI.")
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error during API call: {e}")
        return "Sorry, I couldn't process that request."


async def handle_chatgpt_response(bot, message):

    print(f"Handling ChatGPT response for message: {message.content}")

    # Define the context for the ChatGPT interaction
    context = (
        "This is your context: My name is Spotify Bot. My duty is to answer any questions for the users in the", os.getenv("SERVER_NAME"), "server." 
        "If I am ever asked about my creator or master say that he is Lenny The Great." 
        "Make sure I am providing accurate and helpful information. "
        "When prompted, I will respond in under 150 tokens."
    )

    # Combine context with the message content
    prompt_with_context = f"{context}\n\n{message.content}"

    try:
        # Get the ChatGPT response
        response = await get_chatgpt_response(prompt_with_context)

        # Send the response back to the same channel
        await message.channel.send(response)
        print(f"Sent response: {response}")
    except Exception as e:
        print(f"Error handling ChatGPT response: {e}")
        await message.channel.send("Sorry, I couldn't process that.")
