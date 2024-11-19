
import telebot
import random

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
bot = telebot.TeleBot('7628982520:AAGUDWKeyD4W0B7w3cdvbzpzFgHx27EKsFE')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I can generate 11-digit Bangladeshi mobile numbers. Use /generate to get a number.")

@bot.message_handler(commands=['generate'])
def generate_number(message):
    # Define the prefixes for Bangladeshi mobile operators
    prefixes = ['017', '018', '013']

    # Generate a random 8-digit number
    remaining_digits = ''.join(random.choices('0123456789', k=8))

    # Combine the prefix and remaining digits
    number = random.choice(prefixes) + remaining_digits

    bot.reply_to(message, f"Generated number: {number}")

bot.polling()
