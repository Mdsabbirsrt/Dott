import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import stripe

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Set your Stripe secret key
stripe.api_key = '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'

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Use /charge to make a payment.')

# Charge command handler
def charge(update: Update, context: CallbackContext) -> None:
    try:
        # Assuming the user sends their card details in the message
        card_details = context.args[0]  # Get card details from the command arguments
        amount = 100  # Amount in cents ($1.00)

        # Create a charge
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            source=card_details,  # This should be a token from Stripe.js
            description='Charge for $1.00'
        )
        
        update.message.reply_text('Charge successful!')

    except stripe.error.CardError as e:
        # The card has been declined
        update.message.reply_text('Card charge declined. Please try again.')

    except Exception as e:
        logger.error(f'Error: {e}')
        update.message.reply_text('An error occurred. Please try again later.')

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("7628982520:AAGUDWKeyD4W0B7w3cdvbzpzFgHx27EKsFE")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("charge", charge))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()
