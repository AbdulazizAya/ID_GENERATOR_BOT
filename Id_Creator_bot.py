from telegram import Update,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import Application,CommandHandler,MessageHandler,filters,CallbackContext

Bot_Token = "7995091500:AAGANzqrf1FnN7ddwULypQ2YJ8N8FSvSagQ"

async def start(update:Update , context: CallbackContext):

    option_1 = InlineKeyboardButton("Tech +",url = "https://t.me/Tech_plus_amharic")
    option_2 = InlineKeyboardButton("CONNECT",url = "https://t.me/C_ONNEC_T")
    Keyboard = [[option_1,option_2]]

    reply_markup = InlineKeyboardMarkup(Keyboard)

    user = update.message.from_user
    await update.message.reply_text(f"You must join these channels to use the bot",reply_markup = reply_markup)

async def submit_photo(update:Update , context:CallbackContext):
    await update.message.reply_text("Please send me your photo for the ID.")

async def Submit_name(update:Update,context:CallbackContext):
    await update.message.reply_text("Please Type your Full Name as it should appear on the ID.")

async def help(update:Update,context:CallbackContext):
    
    await update.message.reply_text("Use these commands to Use the bot :\n"
                                    "/start to start the bot.\n"
                                    "/submitphoto to send the photo for your ID.\n"
                                    "/submitname to send your name. ")

async def handle_message(update:Update,context:CallbackContext):
    User_text = update.message.text.lower()
    if "hello" in User_text:
        response = "Hey👋, How are you doing today??"
    elif "how are you" in User_text:
        response = "I am just a bot, but I'm doing great! 😊"
    elif "goodbye" in User_text:
        response = "Good Bye ! Have a Great Day!"
    else:
        response = "Sorry, I don't Understand that."

    await update.message.reply_text(f"{response}")

async def handle_photo(update:Update,context:CallbackContext):
    await update.message.reply_text("Cool pic 📷.")


def main():
    application = Application.builder().token(Bot_Token).build()

    application.add_handler(CommandHandler("start",start))
    application.add_handler(CommandHandler("submitphoto",submit_photo))
    application.add_handler(CommandHandler("submitname",Submit_name))
    application.add_handler(CommandHandler("help",help))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,handle_message))
    application.add_handler(MessageHandler(filters.PHOTO , handle_photo))
    application.run_polling()

if __name__ == '__main__':
    main()
