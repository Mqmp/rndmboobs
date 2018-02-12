import telebot
token = "286888171:AAGb0YLpt_aXbeI3DvjTz7TlASwO0nq49-8"

bot = telebot.TeleBot(token)


bot = telebot.TeleBot(token)

upd = bot.get_updates()
if upd == []:
    while upd == []:
        upd = bot.get_updates()

last_upd = upd[-1]

msg = last_upd.message

@bot.message_handler(content_types = ['text'])
def handle_command(message):
    bot.send_message(msg.chat.id, "ez")

bot.polling(none_stop=True, interval=0)