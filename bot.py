from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from flask import Flask
import threading

TOKEN = "8459414956:AAEifAlppES_CXkE9CqwiCzxnkJ3J1RkiNk"

catalog = """
💎 كتالوج MOTA للاكسسوارات 💎

1- سلسلة 120ج
2- حلق 120ج
3- خاتم 200ج
4- انسيال 220ج
5- سلسلة طويلة 300ج
6- طقم 399ج
7- طقم عروسة 550ج

🚚 شحن 35ج داخل القاهرة
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📖 عرض الكتالوج", callback_data='catalog')],
        [InlineKeyboardButton("📍 عنوان المحل", callback_data='address')],
        [InlineKeyboardButton("💬 تواصل معنا", callback_data='contact')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("أهلا بيك في MOTA ✨ اختار من القائمة:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'catalog':
        await query.message.reply_text(catalog)
    elif query.data == 'address':
        await query.message.reply_text("📍 الجيزة - شارع المحطة\n🕒 من 10 صباحا لـ 10 مساء")
    elif query.data == 'contact':
        await query.message.reply_text("💬 للتواصل: @mota_support")

app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)

def main():
    threading.Thread(target=run_flask).start()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == '__main__':
    main()
