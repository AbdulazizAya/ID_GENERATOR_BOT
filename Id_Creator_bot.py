from telegram import Update,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import Application,CommandHandler,MessageHandler,filters,CallbackContext

Bot_Token = "7995091500:AAGANzqrf1FnN7ddwULypQ2YJ8N8FSvSagQ"

async def start(update:Update , context: CallbackContext):
    user = update.message.from_user
    await update.message.reply_text(f"Hello👋 {user.first_name}, Welcome to the bot!")

async def submit_photo(update:Update , context:CallbackContext):
    await update.message.reply_text("Please send me your photo for the ID.")

async def Submit_name(update:Update,context:CallbackContext):
    await update.message.reply_text("Please Type your Full Name as it should appear on the ID.")

    


def main():
    application = Application.builder().token(Bot_Token).build()

    application.add_handler(CommandHandler("start",start))
    application.add_handler(CommandHandler("Submit",submit_photo))
    application.add_handler(CommandHandler("Submitname",Submit_name))
    
    application.run_polling()

if __name__ == '__main__':
    main()
