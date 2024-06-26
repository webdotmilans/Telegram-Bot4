import telebot
import openai
import os
from dotenv import load_dotenv

load_dotenv()

BOT_API = os.getenv("BOT_API")
OPENAI_KEY = os.getenv("OPENAI_KEY")

chatStr = ''

def ChatModal(prompt):
    global chatStr
    openai.api_key = OPENAI_KEY
    chatStr += f"milan: {prompt}\nJarvis: "
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    chatStr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, "Hello welcome to new bot")

@bot.message_handler()
def chat(message):
    try:
        reply = ChatModal(message.text)
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, e)

print("Bot Started...")
