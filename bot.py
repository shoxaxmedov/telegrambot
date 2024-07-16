import logging
from telegram import Update, ChatJoinRequest
from telegram.ext import Application, CommandHandler, ChatJoinRequestHandler

TOKEN = '7320239291:AAEeSE1fbtaUmfm8hbEwH0dRm12WlSwkug0'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context):
    await update.message.reply_text('Assalomu alaykum! Botga xush kelibsiz!')

async def approve_join_request(update: Update, context):
    chat_join_request = update.chat_join_request
    if chat_join_request:
        chat_id = chat_join_request.chat.id
        user_id = chat_join_request.from_user.id
        try:
            await context.bot.approve_chat_join_request(chat_id, user_id)
            logger.info(f"Foydalanuvchi {user_id} uchun qo'shilish so'rovi tasdiqlandi chat_id {chat_id}")
        except Exception as e:
            logger.error(f"Qo'shilish so'rovini tasdiqlashda xatolik: {e}")

async def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(ChatJoinRequestHandler(approve_join_request))

    logger.info("Bot ishga tushmoqda")
    await application.start_polling()
    await application.wait_for_shutdown()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
