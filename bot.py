from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть калькулятор", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    await update.message.reply_text("Нажмите кнопку ниже, чтобы открыть калькулятор 👇", reply_markup=InlineKeyboardMarkup(keyboard))

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    print("✅ Бот запущен")
    app.run_polling()
