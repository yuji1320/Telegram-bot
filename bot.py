from telebot import TeleBot, apihelper

# توکن ربات تلگرام
TOKEN = "8592104314:AAGVoXhgaHqwxx4aXW-MhjTot8Psah3iHSQ"

# Chat ID شما (ادمین)
ADMIN_ID = 7914359763

bot = TeleBot(TOKEN)

# هر پیام از کاربر → ارسال به ادمین
@bot.message_handler(func=lambda m: True)
def forward_to_admin(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id,"پیامت اومد")

bot.polling(none_stop=True)