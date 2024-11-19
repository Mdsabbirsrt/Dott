import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def gen(update: Update, context: ContextTypes.DEFAULT_TYPE):
  """Generates 6 random numbers from the list [41, 40, 44, 43, 53, 46, 45, 50, 54]."""
  numbers = random.sample([41, 40, 44, 43, 53, 46, 45, 50, 54], 6)
  await update.message.reply_text(f"Your numbers are: {numbers}")

if __name__ == '__main__':
  application = ApplicationBuilder().token('7628982520:AAGUDWKeyD4W0B7w3cdvbzpzFgHx27EKsFE').build()
  
  application.add_handler(CommandHandler('gen', gen))
  
  application.run_polling()
