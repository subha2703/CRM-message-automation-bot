from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8116399803:AAFt0Xh8lU11oJMM2PqXkN5ZU-MXaXd2PmA"  # Replace this with your real bot token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    greeting_message = """
👋 Hi! Welcome to *Cube AI Solutions*\!

🎉 We\'re thrilled to have you join us on this exciting journey of AI & innovation\.

🔗 Stay connected: [Click here to re-open the bot](https://t.me/subhatelegrambot)

Best Regards,  
Cube AI Team 🚀
    """
    await update.message.reply_markdown_v2(greeting_message)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Telegram Greeting Bot is running...")
    app.run_polling()
