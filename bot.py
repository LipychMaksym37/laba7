import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# Завантажуємо .env
load_dotenv()
TOKEN = os.getenv('TOKEN')

async def echo(update, context):
    # Надсилаємо назад те саме повідомлення
    await update.message.reply_text(update.message.text)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Хендлер на всі текстові повідомлення
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()

