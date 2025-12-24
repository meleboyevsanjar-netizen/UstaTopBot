from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8528394369:AAFmS2lNCq7KnuB8NO2e4a82HWFavmFVNxM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Assalomu alaykum!\nUstaTop botiga xush kelibsiz.\n\n/usta - Usta topish\n/ish - Ish berish"
    )

async def usta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠 Usta topish bo‘limi tez orada qo‘shiladi.")

async def ish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 Ish berish bo‘limi tez orada qo‘shiladi.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("usta", usta))
app.add_handler(CommandHandler("ish", ish))

app.run_polling()
