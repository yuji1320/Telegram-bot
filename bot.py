from telebot import TeleBot, apihelper

# پراکسی SOCKS5 فعال
apihelper.proxy = {
    'http':  'socks5://150.227.4.147:1080',
    'https': 'socks5://150.227.4.147:1080'
}

# توکن ربات تلگرام
TOKEN = "8592104314:AAGVoXhgaHqwxx4aXW-MhjTot8Psah3iHSQ"

# Chat ID شما (ادمین)
ADMIN_ID = 7914359763

bot = TeleBot(TOKEN)

# هر پیام از کاربر → ارسال به ادمین
@bot.message_handler(func=lambda m: True)
def forward_to_admin(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "واسه بهروز رفت گلم")

bot.polling(none_stop=True)