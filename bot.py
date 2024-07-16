import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Tokenni muhit o'zgaruvchisidan oling
TOKEN = os.getenv('7320239291:AAEeSE1fbtaUmfm8hbEwH0dRm12WlSwkug0')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # DEBUG darajasiga o'zgartiring
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Received /start command")
    await update.message.reply_text('Bot ishga tushdi!')

async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"New member joined: {update.message.new_chat_members}")
    for member in update.message.new_chat_members:
        try:
            # Foydalanuvchini guruhga qabul qilish
            await context.bot.restrict_chat_member(
                chat_id=update.message.chat_id,
                user_id=member.id,
                permissions={
                    'can_send_messages': True,
                    'can_send_media_messages': True,
                    'can_send_polls': True,
                    'can_send_other_messages': True,
                    'can_add_web_page_previews': True,
                    'can_change_info': False,
                    'can_invite_users': True,
                    'can_pin_messages': False
                }
            )
            logger.info(f"Member {member.full_name} accepted")
            await update.message.reply_text(f'Xush kelibsiz, {member.full_name}!')
        except Exception as e:
            logger.error(f"Error accepting member {member.full_name}: {e}")

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))

    # Qo'shimcha logging uchun
    logger.info("Starting bot application")

    try:
        application.run_polling()
    except Exception as e:
        logger.error(f"Error running bot: {e}")

if __name__ == '__main__':
    main()
