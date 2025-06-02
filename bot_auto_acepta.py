from telegram.ext import Application, ChatJoinRequestHandler

BOT_TOKEN = '7950298628:AAF9W8KJ5NEsn4DMF7JHQkJ6aBm2BPfww4Y'  # <-- pega tu token aquí

async def aprobar(update, context):
    await update.chat_join_request.approve()

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(aprobar))
app.run_polling()
