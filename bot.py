import telebot
import rivescript
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

rs = rivescript.RiveScript()
rs.load_directory("./rivescripts")
rs.sort_replies()

@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_input = message.text
    reply = rs.reply("user", user_input)
    bot.send_message(message.chat.id, reply)

if __name__ == "__main__":
    bot.polling(none_stop=True)
