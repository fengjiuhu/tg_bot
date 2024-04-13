# import telegram
# from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# tk = '7166071452:AAELcgpucqYkO4ayNddHHdkLMiPmNGQxGRg'

# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="欢迎使用我的Bot！")

# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# def error(update, context):
#     print(f"Update {update} caused error {context.error}")

# updater = Updater(token=tk, use_context=True)

# dispatcher = updater.dispatcher

# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

# echo_handler = MessageHandler(filters.text & (~filters.command), echo)
# dispatcher.add_handler(echo_handler)

# dispatcher.add_error_handler(error)

# updater.start_polling()

import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, filters

tk = '7166071452:AAELcgpucqYkO4ayNddHHdkLMiPmNGQxGRg'

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def start_commmand(update, context):
    await update.message.reply_text('Hello! here is me! U can direct ask @Fengj1u OR leave massage with @fengj1u_bot. Thankyou!')
if __name__ == '__main__':
    application = Application.builder().token(tk).build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))

    # Run bot
    application.run_polling(1.0)


