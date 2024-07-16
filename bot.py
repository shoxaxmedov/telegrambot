from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ChatJoinRequestHandler

TOKEN = '7320239291:AAEeSE1fbtaUmfm8hbEwH0dRm12WlSwkug0'

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Assalomu alaykum! Botga xush kelibsiz!')

def approve_join_request(update: Update, context: CallbackContext):
    chat_join_request = update.chat_join_request
    chat_id = chat_join_request.chat.id
    user_id = chat_join_request.from_user.id
    context.bot.approve_chat_join_request(chat_id, user_id)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(ChatJoinRequestHandler(approve_join_request))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
