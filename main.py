from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

# 🔴 BU YERGA YANGI TOKENINGNI QO‘YASAN
TOKEN = "8528394369:AAFmS2lNCq7KnuB8NO2e4a82HWFavmFVNxM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Assalomu alaykum!\n\n"
        "UstaTop botga xush kelibsiz.\n\n"
        "Buyruqlar:\n"
        "/usta – 🛠 Usta chaqirish\n"
        "/ish – 📋 Ish berish"
    )

async def usta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 Usta chaqirish bo‘limi.\n\n"
        "Qanday usta kerakligini yozing."
    )

async def ish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Ish berish bo‘limi.\n\n"
        "Qanday ish borligini yozing."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("usta", usta))
    app.add_handler(CommandHandler("ish", ish))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
