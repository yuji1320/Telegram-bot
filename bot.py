from telebot import TeleBot

TOKEN = "توکن جدید"
ADMIN_ID = 7914359763

bot = TeleBot(TOKEN)

bot.remove_webhook()  # حذف وبهوک در صورت فعال بودن قبلی

@bot.message_handler(func=lambda m: True)
def forward_to_admin(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "پیامت ارسال شد")

bot.polling(none_stop=True)