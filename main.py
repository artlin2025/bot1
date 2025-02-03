import telebot
from telebot import types

TOKEN ="8169426404:AAGo7RX86y1lhglVLSu8HDRlP6D4X2mcfLY"  # 🔹 توکن ربات را جایگزین کن
bot = telebot.TeleBot(TOKEN)

# تابع ساخت منو
def get_main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.row("📖 آموزش جامع پایتون ویژه هفتمی‌ها", "✅ تأیید پرداخت")
    keyboard.row("📞 تماس با پشتیبانی")
    return keyboard

# دستور /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "به ربات خوش آمدید!", reply_markup=get_main_menu())

# نمایش تبلیغ و توضیحات قبل از پرداخت
@bot.message_handler(func=lambda message: message.text == "📖 آموزش جامع پایتون ویژه هفتمی‌ها")
def show_advertisement(message):
    chat_id = message.chat.id
    
    # ارسال عکس تبلیغاتی (مطمئن شو که فایل در کنار کد هست)
    with open("ad.jpg", "rb") as photo:
        bot.send_photo(chat_id, photo, caption="📢 **آموزش جامع پایتون ویژه هفتمی‌ها**\n🚀 بهترین دوره برای یادگیری اصول برنامه‌نویسی به زبان ساده!\n💰 قیمت: 50,000 تومان")
    
    # ایجاد دکمه‌های تأیید یا انصراف
    keyboard = types.InlineKeyboardMarkup()
    btn_yes = types.InlineKeyboardButton("✅ بله، می‌خواهم بخرم", callback_data="confirm_payment")
    btn_no = types.InlineKeyboardButton("❌ خیر، منصرف شدم", callback_data="cancel_payment")
    keyboard.add(btn_yes, btn_no)
    
    bot.send_message(chat_id, "❓ آیا مایل به خرید این آموزش هستید؟", reply_markup=keyboard)

# پردازش دکمه‌های تأیید یا انصراف
@bot.callback_query_handler(func=lambda call: True)
def handle_payment_confirmation(call):
    chat_id = call.message.chat.id

    if call.data == "confirm_payment":
        payment_url = "https://zarinp.al/676109"  # 🔹 لینک زرین‌پال را جایگزین کن
        bot.send_message(chat_id, f"💳 برای خرید، روی لینک زیر کلیک کنید:\n{payment_url}")
    elif call.data == "cancel_payment":
        bot.send_message(chat_id, "✅ مشکلی نیست! هر زمان خواستید، می‌توانید دوباره اقدام کنید.", reply_markup=get_main_menu())

# تأیید پرداخت
@bot.message_handler(func=lambda message: message.text == "✅ تأیید پرداخت")
def confirm_payment(message):
    bot.send_message(message.chat.id, "📌 لطفاً **کد پیگیری تراکنش** خود را ارسال کنید.")

# تماس با پشتیبانی
@bot.message_handler(func=lambda message: message.text == "📞 تماس با پشتیبانی")
def contact_support(message):
    support_info = (
        "☎️ برای تماس با پشتیبانی:\n"
        "📱 شماره: 0912XXXXXXX\n"
        "💬 پشتیبانی تلگرام: @SupportBot\n"
        "📧 ایمیل: artlin2025@gmail.com"
    )
    bot.send_message(message.chat.id, support_info)

# اجرای ربات
bot.polling(none_stop=True)
