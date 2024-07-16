from telegram import Update
from telegram.ext import Updater, CommandHandler, ChatJoinRequestHandler, CallbackContext
import logging

# Tokeningizni kiriting
TOKEN = '7320239291:AAEeSE1fbtaUmfm8hbEwH0dRm12WlSwkug0'

# Logging formatini sozlash
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    logger.info(f"Received /start command from {update.effective_user.id}")
    update.message.reply_text('Assalomu alaykum! Botga xush kelibsiz!')

def approve_join_request(update: Update, context: CallbackContext):
    chat_join_request = update.chat_join_request
    chat_id = chat_join_request.chat.id
    user_id = chat_join_request.from_user.id
    logger.info(f"Received join request from user {user_id} in chat {chat_id}")
    try:
        context.bot.approve_chat_join_request(chat_id, user_id)
        logger.info(f"Approved join request from user {user_id}")
    except Exception as e:
        logger.error(f'Error approving join request: {e}')

def main():
    try:
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(ChatJoinRequestHandler(approve_join_request))

        # Logging uchun xatolarni qayta ishlash
        dp.add_error_handler(error)

        logger.info("Bot is starting")
        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.error(f'Failed to start bot: {e}')

def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

if __name__ == '__main__':
    main()
