from telegram import Update, ChatJoinRequest
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ChatJoinRequestHandler
import logging

TOKEN = '7320239291:AAEeSE1fbtaUmfm8hbEwH0dRm12WlSwkug0'

# Logger o'rnatilishi
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Assalomu alaykum! Botga xush kelibsiz!')

async def approve_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    chat_id = join_request.chat.id
    user_id = join_request.from_user.id
    try:
        await context.bot.approve_chat_join_request(chat_id, user_id)
        logger.info(f"Approved join request for user_id: {user_id} in chat_id: {chat_id}")
    except Exception as e:
        logger.error(f"Error approving join request: {e}")

async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(ChatJoinRequestHandler(approve_join_request))

    logger.info("Bot is starting")
    try:
        await application.initialize()
        await application.start()
        await application.updater.start_polling()
        await application.updater.stop()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")

if __name__ == '__main__':
    import asyncio

    try:
        asyncio.run(main())
    except RuntimeError as e:
        logger.error(f"Runtime error: {e}")
