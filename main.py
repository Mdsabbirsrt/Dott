import telebot
import random

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('7628982520:AAGUDWKeyD4W0B7w3cdvbzpzFgHx27EKsFE')

@bot.message_handler(commands=['nb'])
def generate_bd_number(message):
    # Generate a random 11-digit number starting with 01
    number = '01' + ''.join(random.choices('3456789', k=9))
    bot.reply_to(message, f"Generated BD Number: {number}")

bot.polling()
