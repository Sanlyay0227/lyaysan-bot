from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Вставь сюда свой токен Telegram-бота
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = (
        "Привет! Это бот @Lyaysan_neuro_bot.\n\n"
        "Здесь ты можешь получить PDF-гайд по медленному чтению — пошаговую инструкцию для родителей.\n\n"
        "Нажми кнопку ниже или используй команду /guide, чтобы получить файл."
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)

# Обработчик команды /guide
async def guide(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open("lyaysan_гайд медленное чтение.pdf", "rb") as f:
        await context.bot.send_document(chat_id=update.effective_chat.id, document=f)

# Создание приложения и запуск
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("guide", guide))
    app.run_polling()
