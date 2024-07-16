from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from telegram.ext.filters import StatusUpdate

# Tokenni o'z tokeningiz bilan almashtiring
TOKEN = '7320239291:AAEeSE1fbtaUmfm8hbEwH0dRm12WlSwkug0'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Bot ishga tushdi!')

async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for member in update.message.new_chat_members:
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
        await update.message.reply_text(f'Xush kelibsiz, {member.full_name}!')

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(StatusUpdate.NEW_CHAT_MEMBERS, new_member))

    application.run_polling()

if __name__ == '__main__':
    main()
