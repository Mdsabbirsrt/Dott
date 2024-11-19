import telebot
import random

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('7628982520:AAGUDWKeyD4W0B7w3cdvbzpzFgHx27EKsFE')

@bot.message_handler(commands=['gen'])
def generate_numbers(message):
    try:
        # Get the numbers from the command arguments
        numbers_str = message.text.split('/gen ')[1]
        numbers = [int(num) for num in numbers_str.split(',')]

        # Check if there are enough numbers
        if len(numbers) < 6:
            bot.reply_to(message, "Please provide at least 6 numbers separated by commas.")
            return

        # Generate 6 random numbers from the list
        random_numbers = random.sample(numbers, 6)

        # Send the result
        bot.reply_to(message, f"Your random numbers are: {', '.join(map(str, random_numbers))}")

    except (IndexError, ValueError):
        bot.reply_to(message, "Invalid input. Please use the format /gen number1,number2,..." )

bot.polling()
