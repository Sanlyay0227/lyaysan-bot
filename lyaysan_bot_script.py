
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext

# Insert your bot token here
TOKEN = "8119785184:AAFdnk_cAYJhYsjlYT5TKeh7sRscqJ-unzI"

# Path to your local PDF file
PDF_PATH = "lyaysan_guide_slow_reading.pdf"

# Start command
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Привет! Это бот @Lyaysan_neuro_bot.\n\n"
            "Здесь ты можешь получить PDF-гайд по медленному чтению — пошаговую инструкцию для родителей".

"
            "Нажимаю кнопку ниже или используй команду /guide чтобы получить файл."
        )
    )

# Guide command
def send_guide(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    with open(PDF_PATH, 'rb') as pdf_file:
        context.bot.send_document(
            chat_id=chat_id,
            document=InputFile(pdf_file),
            filename="Гайд_медленное_чтение_Lyaysan.pdf",
            caption="Вот твой гайд по медленному чтению. Если возникнут вопросы — пиши!"
        )

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("guide", send_guide))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
