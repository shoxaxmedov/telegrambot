from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ChatMemberHandler, ContextTypes
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
    chat_member = update.chat_member
    if chat_member.new_chat_member.status == 'member':
        chat_id = chat_member.chat.id
        user_id = chat_member.new_chat_member.user.id
        try:
            await context.bot.approve_chat_join_request(chat_id, user_id)
            logger.info(f"Approved join request for user_id: {user_id} in chat_id: {chat_id}")
        except Exception as e:
            logger.error(f"Error approving join request: {e}")

async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(ChatMemberHandler(approve_join_request, ChatMemberHandler.CHAT_MEMBER))

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
