import telebot

TOKEN = '8106968980:AAG6yhihPZwZ7MOOUpbj4s_mCbpSLD1hdMQ'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
