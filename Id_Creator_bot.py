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

async def help(update:Update,context:CallbackContext):
    
    await update.message.reply_text("Use these commands to Use the bot :\n"
                                    "/start to start the bot.\n"
                                    "/submitphoto to send the photo for your ID.\n"
                                    "/submitname to send your name. ")


def main():
    application = Application.builder().token(Bot_Token).build()

    application.add_handler(CommandHandler("start",start))
    application.add_handler(CommandHandler("submitphoto",submit_photo))
    application.add_handler(CommandHandler("submitname",Submit_name))
    application.add_handler(CommandHandler("help",help))
    application.run_polling()

if __name__ == '__main__':
    main()
